# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_imageimport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imageImport',
        ),
    ]
