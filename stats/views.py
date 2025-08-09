from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Sale
from .serializers import SalesStatsSerializer


class SalesStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    # @method_decorator(cache_page(60*2))
    def get(self, request):
        user = request.user
        data = {
            "daily": Sale.objects.daily_sales(user=user),
            "weekly": Sale.objects.weekly_sales(user=user),
            "monthly": Sale.objects.monthly_sales(user=user),
        }

        serialized_data = {period: SalesStatsSerializer(stats).data for period, stats in data.items()}

        return Response(serialized_data)
