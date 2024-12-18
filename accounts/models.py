from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique = True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, null=True,blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# Create your models here.
