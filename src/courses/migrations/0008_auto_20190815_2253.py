# Generated by Django 2.0.13 on 2019-08-16 05:53

import colorful.fields
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190815_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markrange',
            name='color',
        ),
        migrations.AddField(
            model_name='markrange',
            name='color_dark',
            field=colorful.fields.RGBColorField(default='#337AB7', help_text='Color to be used in the dark theme'),
        ),
        migrations.AddField(
            model_name='markrange',
            name='color_light',
            field=colorful.fields.RGBColorField(default='#BEFFFA', help_text='Color to be used in the light theme'),
        ),
        migrations.AlterField(
            model_name='markrange',
            name='days',
            field=models.CharField(default='1,2,3,4,5,6,7', help_text='Comma seperated list of weekdays that this range is active, where Monday=1 and Sunday=7.                    E.g.: "1,3,5" for M, W, F.', max_length=13, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
