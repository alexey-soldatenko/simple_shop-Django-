from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from auth_shop.models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from auth_shop.tokens import account_activation_token
from cart.views import _cart_id
from order.models import Order
from cart.models import Cart


def display_auth(request, param):
	''' функция отображения страницы регистрации/авторизации '''
	return render(request, 'auth.html', {'param':param})

def save(request):
	if request.method == 'POST':
		#получаем данные, убираем лишние пробелы, валидация всех параметров происходит в html-форме
		cart_id = _cart_id(request)
		name = request.POST["name"].strip()
		last_name = request.POST["last_name"].strip()
		email = request.POST["email"].strip()
		phone = request.POST["phone"].strip()
		password1 = request.POST["password1"].strip()
		password2 = request.POST["password2"].strip()
		if password1 == password2:
			#создаём пользователя в базе данных, по умолчанию он неактивен
			user = MyUser.objects.create(username=name, first_name=name, last_name=last_name, email=email, phone=phone, password=password1, cart_id= cart_id)
			user.is_active = False
			user.save()
			#создаём письмо с активационной ссылкой аккаунта
			current_site = get_current_site(request)
			mail_subject = 'Activate your account on site %s' % current_site
			message = render_to_string(
				'activate_message.html',
				{
				'user':(name+' '+last_name),
				'domain': current_site,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user)
				}
				)
			to_email = email
			#отправляем письмо пользователю
			send_mail(
				mail_subject,
				message,
				'your@mail',
				[to_email],
				html_message = message
				)
			return render(request, 'result_activation.html', {"answer":'Пожалуйста подтвердите вашу почту, перейдя по ссылке в письме, для активации вашего аккаунта.'})
		else:
			message = "Проверьте правильность заполнения формы."
			#return redirect('/sign_up', {'message':message, 'param': 'sign_up'})
			return render(request, 'auth.html', {'message':message, 'param': 'sign_up'})
	else:
		return render(request, 'auth.html')

def activate_account(request, uidb64, token):
	''' функция активации аккаунта '''
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = MyUser.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		#аутентификация пользователя
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		login(request, user)
		return render(request, 'result_activation.html', {'answer':'Благодарим, вы прошли проверку вашей почты, теперь ваш аккаунт активен.'})
	else:
		return render(request, 'result_activation.html', {'answer':'Активационная ссылка устарела. Жаль('})

def user_logout(request):
	'''Выход пользователя из системы'''
	logout(request)
	return redirect(request.META.get('HTTP_REFERER'))

def user_login(request):
	''' функция входа пользователя в систему '''
	if request.method == 'POST':
		name = request.POST["name"]
		email = request.POST["email"]
		password = request.POST["password"]
		try:
			user = MyUser.objects.get(username=name, email=email, password = password)
		except:
			message = "Неверно введен логин или пароль."
			return render(request, 'auth.html', {'message':message, 'param': 'login'})
		if not user.is_active:
			return render(request, 'result_activation.html', {'answer':'В данный момент Вы являетесь неактивным участником. Для того, чтобы стать полноправным членом нашего дружного коллектива, подтвердите актуальность своей почты, перейдя по ссылке в отправленном вам письме. Спасибо, что Вы с нами.'})
		else:
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, user)
			return redirect('/')
	else:
		return render(request, 'auth.html')

def display_account(request):
	''' функция отображения личной страницы пользователя '''
	if request.user.is_authenticated:
		name = request.user.username
		email = request.user.email
		password = request.user.password
		user = MyUser.objects.get(username=name, email=email, password = password)
		orders = Order.objects.filter(cart_id=user.cart_id)
		orders_count = orders.count()
		cart_count = Cart.objects.filter(cart_id=user.cart_id).count()
		return render(request, 'my_account.html', {'orders':orders, 'orders_count':orders_count, 'cart_count':cart_count, 'user':user})
	else:
		return redirect('/')
		