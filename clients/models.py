from django.db import models
from django.db import models
from datetime import datetime

# Create your models here.

class Drivers(models.Model):
	name = models.CharField(max_length=25)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=20)
	is_exp = models.BooleanField(default=False)
	hire_date=models.DateTimeField(default=datetime.now,blank=True)

	def __str__(self):
		return self.name