# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_regis', '0003_travel_trips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='travel_from',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='travel_to',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
    ]
