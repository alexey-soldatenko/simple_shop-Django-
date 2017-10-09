from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from cart.forms import AddCartForm
from cart.models import Cart
from auth_shop.models import MyUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def _cart_id(request):
	''' функция для просмотра/установления параметра cart_id в сессии '''
	if 'cart_id' not in request.session:
		request.session["cart_id"] = _get_cart_id()
	return request.session["cart_id"]

def _get_cart_id():
	''' функция для установления зашифрованного 50-символьного слова '''
	cart_id=''
	characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	cart_id_length = 50
	for ch in range(cart_id_length):
		cart_id += characters[random.randint(0, len(characters)-1)]
	return cart_id 

def add_to_cart(request):
	''' функция добавления товара в корзину '''
	if request.method == 'POST':
		form = AddCartForm(request.POST)
		if form.is_valid():
			cart_id = form.cleaned_data["cart_id"]
			product = form.cleaned_data["product"]

			try:
				Cart.objects.get(cart_id=cart_id, product=product)
			except Cart.DoesNotExist:
				cart = Cart.objects.create(cart_id=cart_id, product=product)
				cart.save()
			else:
				return HttpResponse("Уже есть в корзине.")
		else:
				return HttpResponse(form["product"].errors)
	else:
				return HttpResponse("Не пост.")
	return redirect(request.META["HTTP_REFERER"])

def display_cart(request, page=1):
	''' функция отображения содержимого корзины конретного пользователя '''
	if request.user.is_anonymous():
		cart_id = _cart_id(request)
		
	else:
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
	cart_count = Cart.objects.filter(cart_id=cart_id).count()
	cart = Cart.objects.filter(cart_id=cart_id)

	paginator = Paginator(cart, 2)
	try:
		p = paginator.page(page)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		p = paginator.page(1)

	return render(request, 'user_cart.html', {'cart': cart, 'cart_count':cart_count, 'products':p})

def delete_product_in_cart(request, product_id):
	''' функция удаления товара из корзины '''
	if request.user.is_anonymous():
		cart_id = _cart_id(request)
	else:
		user = MyUser.objects.get(username=request.user.username, email=request.user.email, password=request.user.password)
		cart_id = user.cart_id
	try:
		cart = Cart.objects.get(cart_id = cart_id, product=product_id)
		cart.delete()
	except:
		return HttpResponse('bad')
	return redirect(request.META["HTTP_REFERER"])