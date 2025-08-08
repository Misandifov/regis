from rest_framework import serializers
from .models import Supplier, Warehouse, Category, Product
from .validators import validate_numeric_barcode


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    manufacture_date = serializers.DateField(input_formats=['%d.%m.%Y'], required=False)
    expiration_date = serializers.DateField(input_formats=['%d.%m.%Y'], required=False)
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    barcode = serializers.CharField(validators=[validate_numeric_barcode])

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ProductScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'image', 'selling_price']

