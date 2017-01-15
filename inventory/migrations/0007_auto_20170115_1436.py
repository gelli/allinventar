# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20170115_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='artikelnummer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='gewicht',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='hersteller_lieferant',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='laenge',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='leistung',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='preis_ek',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='preis_vk',
            field=models.IntegerField(null=True),
        ),
    ]
