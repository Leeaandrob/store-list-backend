# coding: utf-8
from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class StoresTxt(models.Model):
    content = models.TextField()
    village = models.OneToOneField(Village)


class Store(models.Model):
    name = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    village = models.ForeignKey(Village)
    imagem = models.ImageField(upload_to='stores/', default='')

    def __unicode__(self):
        return self.name
