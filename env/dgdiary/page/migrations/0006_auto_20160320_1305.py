# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20160320_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='photo',
            field=models.FileField(default='/static/placeholder.jpg', upload_to=page.models.content_file_name),
        ),
    ]