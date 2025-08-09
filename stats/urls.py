from django.urls import path
from .views import SalesStatisticsView

urlpatterns = [
    path('', SalesStatisticsView.as_view(), name='sales-statistics'),
]
