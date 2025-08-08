import re
from rest_framework import serializers


def validate_email(value):
    # Django built-in email validator ishlatish o‘rniga regex ishlatyapmiz
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, value):
        raise serializers.ValidationError("Email manzil noto‘g‘ri formatda.")
    return value
