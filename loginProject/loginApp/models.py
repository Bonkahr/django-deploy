from django.db import models

# Create your models here.


class NewUser(models.Model):
    first_name = models.CharField(max_length=10, unique=False)
    second_name = models.CharField(max_length=10, unique=False)
    user_name = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, unique=True)


class Login(models.Model):
    email = models.EmailField()
