# Generated by Django 3.1.7 on 2021-05-23 14:41

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0020_auto_20210523_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='poylfield',
            field=models.CharField(blank=True, max_length=1111, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
    ]
