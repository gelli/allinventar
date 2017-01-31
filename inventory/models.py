from django.db import models
from decimal import Decimal


# Create your models here.

class MaterialGroup(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class MaterialStatus(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Material(models.Model):
    #    PNummer
    bezeichnung = models.CharField(max_length=100)
    warengruppe = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    gewicht = models.IntegerField(null=True)
    laenge = models.IntegerField(null=True)
    leistung = models.IntegerField(null=True)
    artikelnummer = models.CharField(max_length=50, null=True)
    hersteller_lieferant = models.CharField(max_length=100, null=True)
    #    preis_ek = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    #    preis_vk = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    preis_ek = models.IntegerField(null=True)
    preis_vk = models.IntegerField(null=True)

    def __str__(self):
        return self.bezeichnung


class InventoryItem(models.Model):
    #    ENummer
    identifier = models.CharField(max_length=30)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    status = models.ForeignKey(MaterialStatus, on_delete=models.CASCADE, null=True)
    lager = models.CharField(max_length=10)
    pruefnummer = models.CharField(max_length=30)
    seriennummer = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (self.identifier, self.material.bezeichnung)
