from rest_framework import serializers


def validate_numeric_barcode(value):
    """Barcode faqat raqam bo‘lishini tekshiradi."""
    if not str(value).isdigit():
        raise serializers.ValidationError("Barcode faqat raqamlardan iborat bo‘lishi kerak.")
    return value
