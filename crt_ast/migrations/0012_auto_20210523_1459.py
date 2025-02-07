# Generated by Django 3.1.7 on 2021-05-23 11:59

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0011_auto_20210523_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='geom',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True),
        ),
    ]
