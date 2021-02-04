from django.db import models


class PCHStock(models.Model):
    stock_name = models.CharField(max_length=255)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    average_buy_price = models.CharField(max_length=255)
    average_sell_price = models.CharField(max_length=255)
    net_buy = models.CharField(max_length=255)
    stock_date = models.CharField(max_length=255)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField(null=True)
