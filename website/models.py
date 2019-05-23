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
    texto = models.TextField(max_length=20000, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Descricao/Foto'
        verbose_name_plural='Quem Somos'
        ordering = ['titulo']

class Servicos(models.Model):
    titulo1 = models.CharField(max_length=100, null=True)
    imagem1 = models.ImageField(upload_to='servicos/', null=True, blank=True)
    breveinfo1 = models.CharField(max_length=2000, null=True)
    info1 = models.CharField(max_length=2000, null=True)

    titulo2 = models.CharField(max_length=100, null=True)
    imagem2 = models.ImageField(upload_to='servicos/', null=True, blank=True)
    breveinfo2 = models.CharField(max_length=2000, null=True)
    info2 = models.CharField(max_length=2000, null=True)

    titulo3 = models.CharField(max_length=100, null=True)
    imagem3 = models.ImageField(upload_to='servicos/', null=True, blank=True)
    breveinfo3 = models.CharField(max_length=2000, null=True)
    info3 = models.CharField(max_length=2000, null=True)

    titulo4 = models.CharField(max_length=100, null=True)
    imagem4 = models.ImageField(upload_to='servicos/', null=True, blank=True)
    breveinfo4 = models.CharField(max_length=2000, null=True)
    info4 = models.CharField(max_length=2000, null=True)

    class Meta:
        verbose_name='Descricao'
        verbose_name_plural='Servicos'
        #ordering = ['titulo']

class Portfolio(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    imgdesc = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Descricao/Fotos'
        verbose_name_plural='Portfolio'
        ordering = ['titulo']
