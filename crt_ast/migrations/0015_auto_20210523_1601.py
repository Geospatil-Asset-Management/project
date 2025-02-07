# Generated by Django 3.1.7 on 2021-05-23 13:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Life_Cycle', '0007_auto_20210522_2130'),
        ('crt_ast', '0014_auto_20210523_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326),
        ),
        migrations.AlterField(
            model_name='point',
            name='lc_phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_Life_Cycle.lifecyclephase'),
        ),
    ]
