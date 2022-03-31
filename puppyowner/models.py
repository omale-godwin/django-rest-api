from pydoc import describe
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




class PupOwnerRegistration(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    rating = IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class Puppy(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    vaccinated = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.breed)

class BookedApps(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    time = models.DateTimeField(null=True)
    address = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class EmdeeContact(models.Model):
    fullname = models.CharField(max_length=50)
    feedbacktype = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    def __str__(self):
        return str(self.fullname)

class EmdeeBlog(models.Model):
    imagePath = models.ImageField()
    titleTxt = models.CharField(max_length=50)
    dist = models.DecimalField(max_digits=50, decimal_places=2)
    perNight = models.DecimalField(max_digits=50, decimal_places=2)
    rating = models.DecimalField(max_digits=50, decimal_places=2)
    subTxt = models.TextField(blank=True)
    reviews = models.DecimalField(max_digits=50, decimal_places=2)
    def __str__(self):
        return str(self.titleTxt)
