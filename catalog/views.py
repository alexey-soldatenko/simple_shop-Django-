from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.views import _cart_id, _get_cart_id
from cart.models import Cart
from auth_shop.models import MyUser
import itertools 

# Create your views here.

def display_home(request):
	''' Домашняя страница это - каталог товаров'''
	return redirect("/catalog")

def display_catalog(request, page=1):
	''' Отображает основную страницу сайта'''
	if request.user.is_anonymous():
		#получаем из сесии значение cart_id, если нет, тогда назначаем
		cart_id = _cart_id(request)
	else:
		# если пользователь авторизирован берем cart_id (идентификатор корзины) из базы дынных и сохраняем его в сессии
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
		request.session["cart_id"]= cart_id
	cart_count = Cart.objects.filter(cart_id = cart_id).count()
	cart = Cart.objects.filter(cart_id = cart_id)
	#список товаров в корзине пользователя с определенным cart_id
	cart_products =[]
	for i in cart:
		cart_products.append(i.product.id)
	products = Product.objects.all()
	paginator = Paginator(products, 2)

	page = page
	try:
		p = paginator.page(page)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		p = paginator.page(1)


	return render(request, 'home.html', {'products': p, 'cart_count':cart_count, 'cart_products':cart_products})

def display_404(request):
	return render(request, '404.html')

def display_product_page(request, manufacturer, product_slug):
	''' Отображение страницы товара '''
	if request.user.is_anonymous():
		cart_id = _cart_id(request)
	else:
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
		request.session["cart_id"]= cart_id
	cart_count = Cart.objects.filter(cart_id=cart_id).count()
	product = Product.objects.get(slug=product_slug)
	#считаем размер взносов в месяц при оформлении рассрочки на 12 мес
	cost_month = int(product.has_price/12)
	try:
		#смотрим есть ли у пользователя данный товар в корзине 
		Cart.objects.get(product = product.id, cart_id = cart_id)
		in_cart = True
	except Cart.DoesNotExist:
		in_cart = False
	return render(request, 'product_page.html', {'product':product, 'cost_month': cost_month, 'cart_count': cart_count, 'in_cart':in_cart})

def products_filter(request, *args, **kwargs):
	''' Фильтрация товаров по категориям и признакам '''
	#kwargs - словарь с именами фильтров и их значениями
	#class_list - список с именами фильтров
	class_list = []
	
	page = 1
	if kwargs['page'] is not None:
		page = kwargs['page']
	for i in args:
		
		if type(i) is str:
			class_list.append(i)
		
	#param - список с параметрами конкретного фильтра
	param = []
	#out_dict - 
	out_dict = {}
	for k in kwargs:
		if kwargs[k] is not None:
			#имя фильтра отделено от значений '_', оставшаяся часть - это значения фильтра, поэтому в дальнейшем их поиск будем начинать со значения index
			index = kwargs[k].find('_')
			class_name = k

			if class_name in ['hdd', 'price', 'weight']:
				
				start = kwargs[k].find('-', index)
				min_value = kwargs[k][(index+1): start]
				max_value = kwargs[k][(start+1):-1]
				param.append(min_value)
				param.append(max_value)
				out_dict[class_name] = param
				param = []

			else:
				start = kwargs[k].find('_or_', index)

				if start != -1:
					param = kwargs[k][index+1:-1].split('_or_')
					
				else:
					param.append(kwargs[k][index+1:-1])
					
				'''for i in range(len(kwargs[k][index:])):
					start = kwargs[k].find('_or_', index)

					if start != -1:
						end = kwargs[k].find('_or_', index)
					
						param.append(kwargs[k][index+1:end])
						index = start+3

					else:
						param.append(kwargs[k][index+1:-1])
						break'''

				if param != []:
					out_dict[class_name] = param
				param = []


	products = set()

	all_products = Product.objects.all()

	
	#в итоге получили словарь out_dict с именами фильтров и их значениями, далее извлекаем соответствующие данные из базы данных и укладываем их в frozenset() и в общий set(), чтобы избежать повторений.
	for k, v in out_dict.items():
		if k in ['hdd', 'weight']:
			if k == 'hdd': 
				name = HDD.objects.filter(value__range=(v[0], v[1]))
			elif k == 'weight':
				name = Weight.objects.filter(value__range=(v[0], v[1]))
			for i in name:
				products.add(frozenset(Product.objects.filter(**{k:i.id})))

		elif k == 'price':
			if v[0] < v[1]:
				products.add(frozenset(Product.objects.filter(has_price__range=(v[0], v[1]))))
			else:
				products.add(frozenset(Product.objects.filter(has_price__range=(v[1], v[0]))))

		else:
			for i in v:
				if k == 'manufacturer':
					name = Manufacturer.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
					name = []
				if k == 'kind':
					name = Kind.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
				if k == 'diagonal':
					val = float(v[0])
					p1 = str(val)
					p2 = str(val+1)
					try:
						name = Diagonal.objects.filter(value__range=(p1, p2))
						for i in name:
							products.add(frozenset(Product.objects.filter(**{k:i.id})))
					except:
						pass
				if k == 'display':
					name = Display.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
				if k == 'processor':
					name = Processor.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
				if k == 'ram':
					name = RAM.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
				if k == 'grafic':
					name = Grafic.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
					
				if k == 'dvd':
					name = DVD.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
				if k == 'os':
					name = OS.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))
				if k == 'webcam':
					name = WebCam.objects.get(value=i)
					products.add(frozenset(Product.objects.filter(**{k:name.id})))

	productss = set(itertools.chain.from_iterable(products))
	# преобразовуем set() в list()
	#productss - конечный список товаров
	productss = list(productss)

	if request.user.is_anonymous():
		cart_id = _cart_id(request)
	else:
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
		request.session["cart_id"]= cart_id
	cart_count = Cart.objects.filter(cart_id = cart_id).count()
	cart = Cart.objects.filter(cart_id = cart_id)
	cart_products =[]
	for i in cart:
		cart_products.append(i.product.id)
	
	paginator = Paginator(productss, 1)
	
	try:
		p = paginator.page(page)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		p = paginator.page(1)
	#return HttpResponse(productss)
	return render(request, 'home.html', {'products': p, 'cart_count':cart_count, 'cart_products':cart_products})




def display_our_shops(request, param):
	''' функция для просмотра страниц с дополнительной информацией'''
	#param - параметр, который говорит какая именно страница была запрошена
	if request.user.is_anonymous():
		cart_id = _cart_id(request)
	else:
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
		request.session["cart_id"]= cart_id
	cart_count = Cart.objects.filter(cart_id=cart_id).count()
	return render(request, 'our_shops.html', {'param':param, 'cart_count':cart_count})


