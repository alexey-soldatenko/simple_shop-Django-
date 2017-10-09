from django import forms 

class OrderForm(forms.Form):
	name = forms.CharField(label='Ваше имя', max_length=100)
	lastname = forms.CharField(label='Ваша фамилия', max_length=100)
	e_mail = forms.EmailField(label='Эл.почта')
	phone = forms.IntegerField(label='Номер телефона', help_text='Введите ваш номер телефона')