# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VerifyCode',
            new_name='SmsVerifyCode',
        ),
    ]
