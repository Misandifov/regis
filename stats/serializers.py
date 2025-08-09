from rest_framework import serializers


class SalesStatsSerializer(serializers.Serializer):
    total_quantity = serializers.IntegerField(allow_null=True)
    total_revenue = serializers.DecimalField(max_digits=15, decimal_places=2, allow_null=True)
    total_profit = serializers.DecimalField(max_digits=15, decimal_places=2, allow_null=True)
