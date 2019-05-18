from __future__ import unicode_literals
from django.db import models

class Clientes(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='clientes/', null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True) 

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Fotos'
        verbose_name_plural='Clientes'
        ordering = ['titulo']

class QuemSomos(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.ImageField(upload_to='quemsomos/', null=True, blank=True)
    texto = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Descricao/Foto'
        verbose_name_plural='Quem Somos'
        ordering = ['titulo']

class Servicos(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    breveinfo = models.CharField(max_length=200)
    info = models.CharField(max_length=2000)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Descricao'
        verbose_name_plural='Servicos'
        ordering = ['titulo']

class Portfolio(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='midia/portfolio', null=True, blank=True)
    imgdesc = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Descricao/Fotos'
        verbose_name_plural='Portfolio'
        ordering = ['titulo']
