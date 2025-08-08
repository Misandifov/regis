from django.urls import path
from .views import (
    SupplierListCreateView, SupplierDetailView,
    WarehouseListCreateView, WarehouseDetailView,
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView, ProductScanView,
)

urlpatterns = [
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),

    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('scan/<str:barcode>/', ProductScanView.as_view(), name='product-scan'),
]
