from django.db import models 
from django.contrib.auth.models import User

class MyUser(User):
	phone = models.CharField(max_length=20)
	cart_id = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name

	class Meta:
		db_table = 'my_users'
		ordering = ['first_name']
