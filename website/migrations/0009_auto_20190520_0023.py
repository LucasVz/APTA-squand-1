# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-20 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190520_0021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicos',
            options={'verbose_name': 'Descricao', 'verbose_name_plural': 'Servicos'},
        ),
        migrations.RenameField(
            model_name='servicos',
            old_name='titulo',
            new_name='titulo1',
        ),
        migrations.AddField(
            model_name='servicos',
            name='titulo2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicos',
            name='titulo3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicos',
            name='titulo4',
            field=models.CharField(max_length=100, null=True),
        ),
    ]