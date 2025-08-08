from django.contrib import admin
from .models import Supplier, Warehouse, Category, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'phone_number')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category', 'warehouse', 'supplier', 'quantity', 'cost_price', 'selling_price', 'expiration_date')
    readonly_fields = ('created_at', 'updated_at')
