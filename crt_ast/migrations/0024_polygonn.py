# Generated by Django 3.1.7 on 2021-05-24 07:29

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Life_Cycle', '0007_auto_20210522_2130'),
        ('crt_ast', '0023_auto_20210523_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='polygonn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('geo', models.CharField(max_length=500)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('color', colorfield.fields.ColorField(blank=True, choices=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#808080', 'grey'), ('#FFFF00', 'yellow'), ('#FF0000', 'red'), ('#0000FF', 'blue'), ('#008000', 'green'), ('#FFA500', 'orange'), ('#D4F1F9', 'water')], default='#FFFFFF', max_length=18, null=True)),
                ('lc_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_Life_Cycle.lifecyclephase', verbose_name='Life Cycle Phase')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.assettype')),
            ],
        ),
    ]
