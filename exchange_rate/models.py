from django.db import models

class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length=4)
    base_currency_name = models.CharField(max_length=200)
    other_currency = models.CharField(max_length=4)
    other_currency_name = models.CharField(max_length=200)
    exchange_rate = models. DecimalField(max_digits=20, decimal_places=15)

    def __unicode__(self):
        return self.other_currency
