# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-22 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20190521_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/portfolio'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/clientes'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/portfolio'),
        ),
        migrations.AlterField(
            model_name='quemsomos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='media/quemsomos'),
        ),
    ]