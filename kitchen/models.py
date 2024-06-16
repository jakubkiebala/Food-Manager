import datetime

from django.db import models

# Create your models here.


class Magazine(models.Model):
    name = models.CharField(max_length=150)
    is_cooler = models.BooleanField(default=False)


class MagazineProduct(models.Model):
    name = models.CharField(max_length=150)
    expiration_date = models.DateField()
    received_date = models.DateField(default=datetime.date.today)
    is_opened = models.BooleanField(default=False)
    opened_date = models.DateField(null=True, blank=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.is_opened and self.opened_date is None:
            self.opened_date = datetime.date.today
        super().save(*args, **kwargs)

    def status(self):
        if self.is_opened:
            return 'Otwarto'
        else:
            return 'Zamknięty'

    def open_status(self):
        if not self.opened_date:
            return ''

    def get_status(self):
        how_much_days = (datetime.date.today() - self.received_date).days
        return f'{how_much_days} dni'
