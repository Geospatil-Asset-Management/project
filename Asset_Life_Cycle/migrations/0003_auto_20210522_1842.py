# Generated by Django 3.1.7 on 2021-05-22 15:42

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Life_Cycle', '0002_lifecycle_asset_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifecyclephase',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFFFF', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='lifecyclephase',
            name='lc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_Life_Cycle.lifecycle'),
        ),
    ]
