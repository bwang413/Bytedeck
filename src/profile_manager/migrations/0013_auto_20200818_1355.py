# Generated by Django 2.2.13 on 2020-08-18 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0012_auto_20200807_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='game_lab_transfer_process_on',
            new_name='not_earning_xp',
        ),
    ]
