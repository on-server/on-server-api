# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftp', '0002_auto_20161126_1202'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ftpaccess',
            table='ftp_access',
        ),
        migrations.AlterModelTable(
            name='ftpgroup',
            table='ftp_group',
        ),
        migrations.AlterModelTable(
            name='ftpuser',
            table='ftp_user',
        ),
    ]
