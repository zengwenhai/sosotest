# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-06-03 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_models_for_dubbo', '0003_auto_20190530_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb2dubbotestcasestep',
            name='stepSwitch',
            field=models.IntegerField(db_column='stepSwitch', default=1, verbose_name='此步骤是否勾选执行'),
        ),
        migrations.AddField(
            model_name='tb2dubbotestcasestepdebug',
            name='stepSwitch',
            field=models.IntegerField(db_column='stepSwitch', default=1, verbose_name='此步骤是否勾选执行'),
        ),
    ]
