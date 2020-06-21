from django.db import models

class User(models.Model):
	userId=models.IntegerField(primary_key=True)
	first_name=models.CharField(max_length=256)
	last_name=models.CharField(max_length=256)
	status=models.IntegerField(default=1)
