import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('expiration_date', models.DateField()),
                ('received_date', models.DateField(default=datetime.date.today)),
                ('is_opened', models.BooleanField(default=False)),
                ('opened_date', models.DateField(blank=True, null=True)),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.magazine')),
            ],
        ),
    ]