# Generated by Django 3.0.4 on 2020-03-18 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20200318_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration_data',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='registration_data',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 18, 11, 40, 46, 681127, tzinfo=utc)),
        ),
    ]
