from django.db import models

# Create your models here.

class Users(models.Model):
	firstName = models.CharField(max_length = 128)
	lastName = models.CharField(max_length = 128)
	email = models.EmailField(max_length = 264, unique = True)
