
from django.db import models


class Flower(models.Model):
    PAYMENT_MODE = [('ON', 'ONLINE PAYMENT'), ("EMI", "MONTHLY INSTALLMENT")]
    FLOWER_QUANTITY = [('10roses', '1booke'), ('20roses', '1booke'), ('30roses', '3booke')]
    flower_name = models.CharField(max_length=20)
    flower_price = models.IntegerField()
    flat_delivery_date = models.CharField(max_length=10)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)
    flower_quantity = models.CharField(max_length=10, choices=FLOWER_QUANTITY)
