from django.db import models


class PCHStock(models.Model):
    stock_name = models.CharField(max_length=255)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    average_buy_price = models.FloatField()
    average_sell_price = models.FloatField()
    net_buy = models.IntegerField()
    stock_date = models.CharField(max_length=255)
    create_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField(null=True)
