# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20160320_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='title',
            new_name='highlight',
        ),
    ]