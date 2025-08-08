from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.managers import CustomUserManager
from utills.model import CreateUpdateTracker, nb


class User(AbstractBaseUser, PermissionsMixin, CreateUpdateTracker):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, **nb)
    username = models.CharField(max_length=150, **nb)
    first_name = models.CharField(max_length=150, **nb)
    last_name = models.CharField(max_length=150, **nb)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
