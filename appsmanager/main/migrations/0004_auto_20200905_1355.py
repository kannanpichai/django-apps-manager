# Generated by Django 3.0.4 on 2020-09-05 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200905_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='expiry_at',
        ),
        migrations.AlterField(
            model_name='app',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 5, 13, 55, 30, 565545, tzinfo=utc)),
        ),
    ]