import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Magazine(models.Model):
    name = models.CharField(max_length=150)
    is_cooler = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)


class MagazineProduct(models.Model):
    name = models.CharField(max_length=35)
    expiration_date = models.DateField()
    received_date = models.DateField(default=datetime.date.today)
    is_opened = models.BooleanField(default=False)
    opened_date = models.DateField(null=True, blank=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.is_opened and self.opened_date is None:
            self.opened_date = datetime.date.today()
        super().save(*args, **kwargs)

    def status(self):
        if self.is_opened:
            return 'Otwarto'
        else:
            return 'Zamknięty'

    def open_status(self):
        if self.is_opened and self.opened_date:
            return self.opened_date
        else:
            return ''

    def get_status(self):
        how_much_days = (datetime.date.today() - self.received_date).days
        return f'{how_much_days} dni'


class CatalogProduct(models.Model):
    name = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)


class CatalogProducts(models.Model):
    product = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE)
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    stock_level = models.PositiveIntegerField(default=0)


class Catalog(models.Model):
    name = models.CharField(max_length=150)
    products = models.ManyToManyField(CatalogProduct, through='CatalogProducts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
