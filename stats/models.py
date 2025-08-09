from django.db import models

from product.models import Product
from stats.manager import SaleManager
from users.models import User


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sale_date = models.DateTimeField(auto_now_add=True)

    profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.product.selling_price * self.quantity
        self.profit = (self.product.selling_price - self.product.cost_price) * self.quantity
        super().save(*args, **kwargs)

    objects = SaleManager()

    def __str__(self):
        return f"{self.product.title} - {self.quantity} dona sotildi {self.sale_date.strftime('%Y-%m-%d')}"
