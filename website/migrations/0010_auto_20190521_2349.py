# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-21 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20190520_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='imgdesc',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='quemsomos',
            name='texto',
            field=models.TextField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='breveinfo1',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='breveinfo2',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='breveinfo3',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='breveinfo4',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='info1',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='info2',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='info3',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='info4',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
