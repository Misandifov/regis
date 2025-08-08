from django.core.validators import validate_email
from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[validate_email])


class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(min_length=6, write_only=True)
