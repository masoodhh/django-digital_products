from rest_framework import serializers
from .models import Subscription, Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['title', 'sku','description', 'price',  'avatar', 'duration']


class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ['package','created_time', 'expire_time']
