from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length = 30)
    target_currency = models.CharField(max_length = 30)
    value = models.FloatField()
    timestamp = models.DateField()