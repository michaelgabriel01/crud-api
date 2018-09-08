# crudapp/serializers.py

from rest_framework import serializers

# Local import
from . import models


# sku serializer class
class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkuModel
        fields = '__all__'


# available sku serializer class
class AvailableSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableSkuModel
        fields = '__all__'


# notification sku serializer class
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotificationModel
        fields = '__all__'