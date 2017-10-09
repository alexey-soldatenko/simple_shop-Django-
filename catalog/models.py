from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True)
	is_active = models.BooleanField(default=True)
	meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField("Meta description", max_length=255, help_text='Content for description meta tag')

	class Meta:
		db_table = 'categories'
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category', {'category': self.slug})


class Kind(models.Model):
	value = models.CharField(max_length=50, unique=True)

	class Meta:
		db_table = 'kind'

	def __str__(self):
		return self.value

class Manufacturer(models.Model):
	value = models.CharField(max_length=30, unique=True)

	class Meta:
		db_table = 'manufacturer'

	def __str__(self):
		return self.value

class Diagonal(models.Model):
	value = models.DecimalField(unique=True, max_digits=3, decimal_places=1)

	class Meta:
		db_table = 'diagonal'

	def __str__(self):
		return str(self.value)

class Display(models.Model):
	value = models.CharField(max_length=30, unique=True)

	class Meta:
		db_table = 'display'

	def __str__(self):
		return self.value

class Processor(models.Model):
	value = models.CharField(max_length=30, unique=True)

	class Meta:
		db_table = 'processor'

	def __str__(self):
		return self.value

class RAM(models.Model):
	value = models.IntegerField(unique=True)

	class Meta:
		db_table = 'ram'

	def __str__(self):
		return str(self.value)

class Grafic(models.Model):
	value = models.CharField(max_length=20, unique=True)

	class Meta:
		db_table = 'grafic'

	def __str__(self):
		return self.value

class HDD(models.Model):
	value = models.IntegerField(unique=True)

	class Meta:
		db_table = 'hdd'

	def __str__(self):
		return str(self.value)

class DVD(models.Model):
	value = models.CharField(max_length=10, unique=True)

	class Meta:
		db_table = 'dvd'

	def __str__(self):
		return self.value

class OS(models.Model):
	value = models.CharField(max_length=15, unique=True)

	class Meta:
		db_table = 'os'

	def __str__(self):
		return self.value

class WebCam(models.Model):
	value = models.CharField(max_length=15, unique=True)

	class Meta:
		db_table = 'webcam'

	def __str__(self):
		return self.value

class Weight(models.Model):
	value = models.DecimalField(unique=True, max_digits=3, decimal_places=1)

	class Meta:
		db_table = 'weight'

	def __str__(self):
		return str(self.value)





class Product(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey(Category)
	description = models.TextField()
	code = models.PositiveIntegerField(default=1111)
	meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')
	is_active = models.BooleanField(default=True)
	number_in_store = models.PositiveSmallIntegerField()
	was_price = models.PositiveIntegerField(default=0)
	has_price =  models.IntegerField()
	create_date = models.DateField(auto_now_add=True)
	update_date = models.DateField(auto_now=True)
	kind = models.ForeignKey(Kind)
	manufacturer = models.ForeignKey(Manufacturer)
	diagonal = models.ForeignKey(Diagonal)
	display = models.ForeignKey(Display)
	processor = models.ForeignKey(Processor)
	ram = models.ForeignKey(RAM)
	grafic = models.ForeignKey(Grafic)
	hdd = models.ForeignKey(HDD)
	dvd = models.ForeignKey(DVD)
	os = models.ForeignKey(OS)
	webcam = models.ForeignKey(WebCam)
	weight = models.ForeignKey(Weight)

	class Meta:
		db_table = 'product'
		ordering = ['name', 'is_active']


	def get_absolute_url(self):
		return reverse('product', {'product': self.slug})

	def __str__(self):
		return self.name
		