from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class userAbstract(AbstractUser):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    # username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.email
 