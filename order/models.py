from django.db import models
from catalog.models import Product

# Create your models here.
class Order(models.Model):
	cart_id = models.CharField(max_length=50)
	quantity = models.PositiveSmallIntegerField(default=1)
	product = models.ForeignKey(Product)
	user_name = models.CharField(max_length=50)
	user_lastname = models.CharField(max_length=70)
	phone_number = models.CharField(max_length=20)
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)
	
