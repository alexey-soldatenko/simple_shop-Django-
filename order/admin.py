from django.contrib import admin
from order.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	list_display = ['cart_id', 'product', 'quantity', 'date']

admin.site.register(Order, OrderAdmin)