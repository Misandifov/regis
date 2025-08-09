from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from users.managers import UserManager
from utills.model import CreateUpdateTracker, nb


class User(AbstractUser, CreateUpdateTracker):
    username = None  # AbstractUser dan kelgan maydonni olib tashlaymiz
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # superuser yaratishda faqat email va password so'raladi

    objects = UserManager()

    def __str__(self):
        return self.email
