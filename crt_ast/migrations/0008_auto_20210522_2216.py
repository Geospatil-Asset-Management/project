# Generated by Django 3.1.7 on 2021-05-22 19:16

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0007_auto_20210522_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
    ]
