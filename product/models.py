from django.db import models

from users.models import User
from utills.model import nb, CreateUpdateTracker


class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_supplier')
    title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, **nb)
    description = models.CharField(max_length=255, **nb)

    def __str__(self):
        return self.title


class Warehouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_warehouse')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(CreateUpdateTracker):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(CreateUpdateTracker):
    UNIT_CHOICES = [
        ('dona', 'dona'),
        ('g', 'g'),
        ('kg', 'kg'),
        ('ml', 'ml'),
        ('l', 'l'),
        ('sm', 'sm'),
        ('m', 'm'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')
    title = models.CharField(max_length=255)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    quantity = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='warehouse_products')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    barcode = models.PositiveIntegerField(unique=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_products')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2, **nb)

    manufacture_date = models.DateField(**nb)
    expiration_date = models.DateField(**nb)
    additional_notes = models.CharField(max_length=255, **nb)
    image = models.ImageField(upload_to="images/product/", **nb)

    def __str__(self):
        return f"{self.category.title} - {self.title}"




