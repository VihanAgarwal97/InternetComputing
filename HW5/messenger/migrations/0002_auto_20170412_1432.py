# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sent',
            new_name='is_sent',
        ),
    ]
