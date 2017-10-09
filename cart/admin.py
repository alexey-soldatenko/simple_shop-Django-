from django.contrib import admin
from cart.models import Cart
# Register your models here.

class AdminCart(admin.ModelAdmin):
	list_display = ['cart_id', 'product', 'date_add']

admin.site.register(Cart, AdminCart)