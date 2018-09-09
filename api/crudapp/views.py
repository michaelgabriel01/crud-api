from django.shortcuts import render
from rest_framework import viewsets, routers
from . import serializers
from . import models



# Root API class
class CrudApiRoot(routers.APIRootView):
    """
    This is the ROOT API
    """

# Documented class
class DocumentedApiView(routers.DefaultRouter):
    APIRootView = CrudApiRoot


# sku model view class
class SkuModelView(viewsets.ModelViewSet):
    queryset = models.SkuModel.objects.all()
    serializer_class = serializers.SkuSerializer
    # permission_classes = ()


# available sku model view class
class AvailableSkuModelView(viewsets.ModelViewSet):
    queryset = models.AvailableSkuModel.objects.all()
    serializer_class = serializers.AvailableSkuSerializer
    # permission_classes = ()


# notification model view class
class NotificationModelView(viewsets.ModelViewSet):
    queryset = models.NotificationModel.objects.all()
    serializer_class = serializers.NotificationSerializer
    # permission_classes = ()

def get_notification_view(request):
    try:
        get_update = models.NotificationModel.get_notification()
    except models.NotificationModel.DoesNotExist:
        raise ("Notification does not exist")
    return render(request, 'notification_file.html', {'notification': get_update})