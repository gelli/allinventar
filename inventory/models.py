from django.db import models

# Create your models here.


class MaterialGroup(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Material(models.Model):
    bezeichnung = models.CharField(max_length=100)
    warengruppe = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    gewicht = models.CharField(max_length=30)
    laenge = models.CharField(max_length=30)
    leistung = models.CharField(max_length=30)
    artikelnummer = models.CharField(max_length=30)
    hersteller_lieferant  = models.CharField(max_length=100)
    preis_ek = models.CharField(max_length=30)
    preis_vk = models.CharField(max_length=30)

    def __str__(self):
        return self.bezeichnung

class Inventory(models.Model):
    identifier = models.CharField(max_length=30)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    lager = models.CharField(max_length=30)
    pruefnummer = models.CharField(max_length=30)
    seriennummer = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (self.identifier, self.material.bezeichnung)
