from django.db import models

class Customer(models.Model):
    rate_price = models.FloatField()
    vip_question = models.CharField(max_length=3)
    vip_discount_rate = models.FloatField()
    hour = models.FloatField()
    minute = models.IntegerField()
    cost = models.FloatField()
    discount_enabled = models.BooleanField(default=False)
