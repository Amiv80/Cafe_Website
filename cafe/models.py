from django.db import models

class Customer(models.Model):
    rate_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Rate Price')
    vip_question = models.CharField(max_length=3, verbose_name='VIP Question')
    vip_discount_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='VIP Discount Rate')
    time = models.TimeField(verbose_name='Time')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cost')
    discount_enabled = models.BooleanField(default=False, verbose_name='Discount Enabled')