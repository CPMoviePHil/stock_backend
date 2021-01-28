from django.db import models


class PchStock(models.Model):
    stock_name = models.CharField(max_length=255)
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    average_buy_price = models.IntegerField(default=0)
    average_sell_price = models.IntegerField(default=0)
    net_buy = models.IntegerField(default=0)
