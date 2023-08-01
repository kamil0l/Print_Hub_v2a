from django.db import models

# Create your models here.

class Printer(models.Model):
    name = models.CharField(max_length=123)
    head = models.IntegerField()
    max_temperature = models.IntegerField()
    max_speed = models.IntegerField()
    materials = ()

class Filament(models.Model):
    name = models.CharField(max_length=123)
    producer = models.CharField(max_length=123)
    material = models.CharField(max_length=12)
    colour = models.CharField(max_length=24)
    temperature_min = models.IntegerField()
    temperature_max = models.IntegerField()
    weight = models.IntegerField()

class Project(models.Model):
    name = models.CharField(max_length=256)
    printer = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Filament, on_delete=models.SET_NULL, null=True)

class Parts(models.Model):
    name = models.CharField(max_length=123)
    description = models.CharField(max_length=256)
    printer = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True)

