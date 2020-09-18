from django.db import models


class Mitra(models.Model):
    nama = models.CharField(max_length=225)
    alamat = models.CharField( max_length=255)
    status = models.CharField( max_length=255)