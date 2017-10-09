from django import forms 
from catalog.models import Product

class ProductAdminForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

	def clean_has_price(self):
		if self.cleaned_data['has_price'] <= 0:
			raise forms.ValidationError('Цена должна быть выше нуля.')
		return self.cleaned_data['has_price']

class ProductAddToCartForm(forms.ModelForm):
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity', 'maxlength':'5'}), error_messages={'invalid':'Please enter a valid quantity'}, min_value=1)
	product_slug = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		super(ProductAddToCartForm, self).__init__(*args, **kwargs)

	def clean(self):
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError('Cookie must be enabled')
		return self.cleaned_data

