from django.db import models

# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    estb_year = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=80)


