# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-25 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boards',
            new_name='Board',
        ),
    ]