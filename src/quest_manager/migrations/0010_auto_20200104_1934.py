# Generated by Django 2.2.9 on 2020-01-05 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_manager', '0009_auto_20190807_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='date_available',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
