from django.contrib import admin
from catalog.models import * 
from catalog.forms import ProductAdminForm

# Register your models here.
admin.site.register(Category)
admin.site.register(Kind)
admin.site.register(Manufacturer)
admin.site.register(Diagonal)
admin.site.register(Display)
admin.site.register(Processor)
admin.site.register(RAM)
admin.site.register(Grafic)
admin.site.register(HDD)
admin.site.register(DVD)
admin.site.register(OS)
admin.site.register(WebCam)
admin.site.register(Weight)


class AdminProduct(admin.ModelAdmin):
	form = ProductAdminForm
	list_display = ['name', 'category', 'has_price', 'create_date', 'number_in_store']

admin.site.register(Product, AdminProduct)