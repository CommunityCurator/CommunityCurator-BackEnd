from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class User(AbstractBaseUser):
    userName = models.CharField(max_length=30, unique=True)
    firstName = models.CharField(max_length=35, blank=True)
    lastName = models.CharField(max_length=35, blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(max_length=20)
    bio = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=100, blank=True)
    createdAt = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    groups = models.ManyToManyField('group.Group', blank=True)

    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ['email']
