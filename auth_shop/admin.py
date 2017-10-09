from django.contrib import admin 
from auth_shop.models import MyUser

class MyUserAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'phone', 'email', 'cart_id']

admin.site.register(MyUser, MyUserAdmin)
