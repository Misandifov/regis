from django.db import models
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta


class SaleManager(models.Manager):
    def sales_in_period(self, days, user=None):
        today = timezone.now().date()
        start_date = today - timedelta(days=days)
        qs = self.filter(sale_date__date__gte=start_date)
        if user is not None:
            qs = qs.filter(user=user)
        return qs.aggregate(
            total_quantity=Sum('quantity'),
            total_revenue=Sum('total_price'),
            total_profit=Sum('profit')
        )

    def daily_sales(self, user=None):
        return self.sales_in_period(1, user=user)

    def weekly_sales(self, user=None):
        return self.sales_in_period(7, user=user)

    def monthly_sales(self, user=None):
        return self.sales_in_period(30, user=user)
