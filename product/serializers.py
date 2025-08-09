from rest_framework import serializers

from stats.models import Sale
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
    action = serializers.ChoiceField(choices=['confirm'], write_only=True)
    current_quantity = serializers.IntegerField(required=False, default=1, write_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'selling_price', 'total_price', 'action', 'current_quantity']
        read_only_fields = ['id', 'title', 'image', 'selling_price', 'quantity']

    def validate_current_quantity(self, value):
        if value is None or value < 1:
            raise serializers.ValidationError("Mahsulot soni 1 dan kam bo‘lishi mumkin emas.")
        return value

    def validate(self, attrs):
        instance = self.instance
        current_quantity = attrs.get('current_quantity', 1)

        if instance and current_quantity > instance.quantity:
            raise serializers.ValidationError(
                f"Maksimal {instance.quantity} dona mahsulot mavjud."
            )

        return attrs

    def update(self, instance, validated_data):
        action = validated_data.get('action')
        current_quantity = validated_data.get('current_quantity', 1)

        if action != 'confirm':
            raise serializers.ValidationError("Faqat 'confirm' amaliga ruxsat berilgan.")

        instance.quantity -= current_quantity
        instance.save()

        sale = Sale.objects.create(
            user=self.context['request'].user,
            product=instance,
            quantity=current_quantity
        )

        instance._current_quantity = current_quantity
        return instance

    def get_total_price(self, instance):
        current_quantity = getattr(instance, "_current_quantity", None)
        if current_quantity is None:
            # Agar update emas, oddiy GET bo‘lsa total_price 0 chiqadi
            return 0
        return instance.selling_price * current_quantity
