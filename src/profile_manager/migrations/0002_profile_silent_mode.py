# Generated by Django 2.0.10 on 2019-01-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='silent_mode',
            field=models.BooleanField(default=False, help_text="Don't play the gong sounds."),
        ),
    ]
