# Generated by Django 5.0.6 on 2024-06-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0012_catalogproduct_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogproducts',
            name='stock_level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
