from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Times(models.Model):
	date 		= models.DateField(auto_now=False, auto_now_add=False)
	time		= models.DateField(auto_now=False, auto_now_add=False)

class Class(models.Model):
	name		= models.CharField(max_length=120)
	crn			= models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999),MinValueValidator(10000)])
	subject		= models.CharField(max_length=5)
	course		= models.CharField(max_length=5)
	section 	= models.CharField(max_length=3)
	instructor	= models.CharField(max_length=120)
#	times		= models.ManyToManyField(Times)
