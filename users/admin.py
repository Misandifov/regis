from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ("id", 'email', 'phone_number', 'username', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
