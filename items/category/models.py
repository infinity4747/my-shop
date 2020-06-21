from django.db import models

# Create your models here.

class Category(models.Model):
	categoryId=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=256)
	status=models.IntegerField(default=1)

class Product(models.Model):
	productId=models.IntegerField(primary_key=True)
	categoryId=models.ForeignKey(Category,on_delete="CASCADE")
	name=models.CharField(max_length=256)
	price=models.IntegerField()
	status=models.IntegerField(default=1)

