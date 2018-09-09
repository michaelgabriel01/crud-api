import requests
from django.db import models


# sku model class
class SkuModel(models.Model):
    type = models.CharField(max_length=20)
    product_name = models.CharField(max_length=30)
    product_id = models.CharField(max_length=10)
    sku_id = models.CharField(max_length=10)
    sent_date = models.DateTimeField()

    def __str__(self, *args, **kwargs):
        data = [self.product_name, self.product_id]
        return 'Product name: {}, Product ID: {}'.format(*data)


# available sku model class
class AvailableSkuModel(models.Model):
    available_sku = models.ForeignKey('SkuModel', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self, *args, **kwargs):
        return '{}, Price: {}'.format(self.available_sku, self.price)

    def get_price(self):
        if self.price in range(10, 41):
            return self.price

    def set_price(self, price):
        self.price = price


# notification model class
# return sku and updated list
class NotificationModel(models.Model):
    notification = models.ForeignKey('SkuModel', on_delete=models.CASCADE)

    def get_notification():
        api_url = "https://sandboxmhubapi.epicom.com.br/v1"
        access_key = "897F8D21A9F5A"
        token = "Ip15q6u7X15EP22GS36XoNLrX2Jz0vqq"
        auth = (access_key, token)
        respones = requests.get(api_url, auth=auth)
        r = respones.text
        file = open('/home/michael/Desktop/Bot/epicom-api/crud-api/api/crudapp/templates/notification_file.html', 'w')
        file.write(r)
        file.close()
        return file

    def update_sku(self):
        api_url = "https://sandboxmhubapi.epicom.com.br/v1"
        data = ""
        access_key = "897F8D21A9F5A"
        token = "Ip15q6u7X15EP22GS36XoNLrX2Jz0vqq"
        auth = (access_key, token)
        respones = requests.post(api_url, auth, data)
        return  respones