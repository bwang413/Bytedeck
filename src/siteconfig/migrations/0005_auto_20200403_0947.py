# Generated by Django 2.2.9 on 2020-04-03 16:47

from django.db import migrations, models
import django.db.models.deletion
import siteconfig.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteconfig', '0004_auto_20200402_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='default_icon',
            field=models.ImageField(blank=True, help_text='This becomes the default icon for quests and badges and other places where icons are used (ideally 256x256 px).If no icon is provided, it will fall back on the site logo (so you can leave this blank if you want to use your logo)', null=True, upload_to='', verbose_name='Default Icon'),
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='active_semester',
            field=models.ForeignKey(default=siteconfig.models.get_active_semester, help_text='Your currently active semester.  New semesters can be created from the admin menu.', on_delete=django.db.models.deletion.SET_DEFAULT, to='courses.Semester', verbose_name='Active Semester'),
        ),
        migrations.AlterField(
            model_name='siteconfig',
            name='site_logo',
            field=models.ImageField(blank=True, help_text="This will be displayed at the top left of your site's header (ideally 256x256 px).", null=True, upload_to='', verbose_name='Site Logo'),
        ),
    ]
