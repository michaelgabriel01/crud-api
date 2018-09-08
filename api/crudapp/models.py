from django.db import models


# sku model class
class SkuModel(models.Model):
    type = models.CharField(max_length=20)
    product_name = models.CharField(max_length=30)
    product_id = models.CharField(max_length=10)
    sku_id = models.CharField(max_length=10)
    sent_date = models.DateTimeField()


# available sku model class
class AvailableSkuModel(models.Model):
    available_sku = models.ForeignKey('SkuModel', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)


# notification model class
# return sku and updated list
class NotificationModel(models.Model):
    notification = models.ForeignKey('SkuModel', on_delete=models.CASCADE)
