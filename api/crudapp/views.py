# from django.shortcuts import render
from rest_framework import viewsets, routers
from . import serializers, models



# Root API class
class CrudApiRoot(routers.APIRootView):
    """
    This is the ROOT API
    """

# Documented class
class DocumentedApiView(routers.DefaultRouter):
    APIRootView = CrudApiRoot


# sku model view class
class SkuModelView(viewsets.ViewSet):
    serializer_class = serializers.SkuSerializer
    # permission_classes = ()
    queryset = models.SkuModel.objects.all()


# available sku model view class
class AvailableSkuModelView(viewsets.ViewSet):
    serializer_class = serializers.AvailableSkuSerializer
    # permission_classes = ()
    queryset = models.AvailableSkuModel.objects.all()


# notification model view class
class NotificationModelView(viewsets.GenericViewSet):
    serializer_class = serializers.NotificationSerializer
    # permission_classes = ()
    queryset = models.NotificationModel.objects.all()