from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from cart.views import _cart_id, _get_cart_id
from catalog.models import Product
from order.models import Order
from cart.models import Cart
from auth_shop.models import MyUser
from django.core.mail import send_mail
from datetime import datetime

# Create your views here.
def display_order(request):
	''' функция отображения страницы заказа товара '''
	if request.user.is_anonymous():
		cart_id = _cart_id(request)
		name = ''
		last_name = ''
		email = ''
		phone = ''
		user_data = [name, last_name, email, phone]
	else:
		#если пользователь авторизирован, автоматически заносим его данные в поля формы заказа
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
		request.session["cart_id"]= cart_id
		name = user.first_name
		last_name = user.last_name
		email = user.email
		phone = user.phone
		user_data = [name, last_name, email, phone]

	cart_count = Cart.objects.filter(cart_id = cart_id).count()
	if request.method == "POST":
		#получаем значение id товара и его количество, переданные после перехода с предыдущей страницы
		product_id = request.POST['product_id']
		num_products = request.POST['num_products']
		product = Product.objects.get(id=product_id)
		return render(request, 'order.html', {'product':product, 'num_products':num_products, 'cart_count':cart_count, 'user_data':user_data})
	else:
		return render(request, 'order.html', {'cart_count':cart_count})

def save_order(request):
	''' функция сохранения заказа в базе данных '''
	if request.user.is_anonymous():
		cart_id = _cart_id(request)
	else:
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
		request.session["cart_id"]= cart_id

	if request.method == 'POST':
		try:
			#извлекаем полученные из формы данные
			name = request.POST["name"].strip()
			last_name = request.POST["last_name"].strip()
			mail = request.POST["email"].strip()
			phone = request.POST["phone"].strip()
			num_products = request.POST["num_products"]
			product_id = int(request.POST["product"])
			date = datetime.now()
		except:
			return HttpResponse("O-o-o, no!")
		else:
			#сохраняем заказ в базе данных 
			product = Product.objects.get(id=product_id)
			order = Order.objects.create(cart_id = cart_id, product= product, quantity= num_products, user_name = name, user_lastname= last_name, phone_number = phone, email = mail)
			order.save()
			#отправляем письмо лицу, обрабатывающему заказы (письмо в html форме будет содержать таблицу с данными о заказе)
			mail_subject = 'New order!'
			mail_message = render_to_string(
				'message_with_order.html',
				{
				'product_name': product.name,
				'product_id': product_id,
				'num_products':num_products,
				'orderer_name': name,
				'orderer_lastname': last_name,
				'mail':mail,
				'phone':phone,
				'date': date
				}
				)
			#адрес почты лица, обрабатывающего заказы
			to_email = '@mail'
			send_mail(
				mail_subject,
				mail_message,
				'your@mail',
				[to_email],
				html_message=mail_message)
			return render(request, 'result.html')




