from django.db import models

# sku model class
class Sku(models.Model):
    type = models.CharField()
    product_name = models.CharField()
    sku_name = models.CharField()
    sku_id = models.CharField()
    sent_date = models.CharField()