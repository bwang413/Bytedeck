# Generated by Django 3.2.13 on 2022-08-12 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20220811_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestudent',
            name='grade_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.grade', verbose_name='Grade'),
        ),
    ]
