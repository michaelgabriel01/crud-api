from django.contrib import admin

# local import
from .models import  SkuModel, AvailableSkuModel, NotificationModel


# register model classes
admin.site.register(SkuModel)
admin.site.register(AvailableSkuModel)
admin.site.register(NotificationModel)
