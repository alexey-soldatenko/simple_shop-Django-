from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.models import Cart
from cart.views import _cart_id
from catalog.models import Product
import itertools 

# Create your views here.
def display_search(request):
	''' функция отображающая страницу с результатами поиска '''
	cart_id = _cart_id(request)
	cart_count = Cart.objects.filter(cart_id = cart_id).count()
	cart = Cart.objects.filter(cart_id = cart_id)
	#список товаров в корзине пользователя с определенным cart_id
	cart_products =[]
	for i in cart:
		cart_products.append(i.product.id)
	if request.method == 'GET':
		#выполняем поиск отдельно по словам
		search_words = request.GET["search"].split(' ')
		try:
			page = request.GET["page"]
		except:
			page = 1
		products = []
		for word in search_words:
			products.append(Product.objects.filter(description__icontains=word))
		#разворачиваем содержимое списков во множестве, чтобы избежать дубликатов и обратно преобразуем в список
		productss = set(itertools.chain.from_iterable(products))
		productss = list(productss)

		paginator = Paginator(productss, 2)
		
		try:
			p = paginator.page(page)
		except EmptyPage:
			p = paginator.page(paginator.num_pages)
		except PageNotAnInteger:
			p = paginator.page(1)
		search = '?search='+request.GET["search"]
		
	return render(request, 'search.html', {'products': p, 'cart_count':cart_count, 'search': search, 'cart_products':cart_products})