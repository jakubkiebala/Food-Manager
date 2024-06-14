from django.db import models

# Create your models here.


class Magazine(models.Model):
    name = models.CharField(max_length=150)
    is_cooler = models.BooleanField(default=False)
