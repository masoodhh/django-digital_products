from rest_framework import serializers
from .models import Payment, Gateway


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'package', 'gateway', 'price', 'status', 'device_uuid', 'token', 'phone_number', 'consumed_code', 'created_time', 'updated_time']


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ['id', 'name', 'description', 'is_active', 'created_time', 'updated_time']