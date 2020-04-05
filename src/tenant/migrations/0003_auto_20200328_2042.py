# Generated by Django 2.2.11 on 2020-03-29 03:42

from django.db import migrations, models
import tenant_schemas.postgresql_backend.base


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_tenant_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='domain_url',
            field=models.CharField(editable=False, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[tenant_schemas.postgresql_backend.base._check_schema_name]),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='schema_name',
            field=models.CharField(editable=False, max_length=63, unique=True, validators=[tenant_schemas.postgresql_backend.base._check_schema_name]),
        ),
    ]
