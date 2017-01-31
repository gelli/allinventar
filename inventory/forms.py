from django import forms

from .models import MaterialGroup


class NewEinzelbuchungForm(forms.Form):
    materialgruppe = forms.ModelChoiceField(queryset=MaterialGroup.objects.all(), required=True)
    bezeichnung = forms.CharField(max_length=100)
    lager = forms.IntegerField(max_value=100, min_value=0)
    nebenlager = forms.IntegerField(max_value=100, min_value=0)
    gewicht = forms.IntegerField(max_value=100, min_value=0)
    länge = forms.IntegerField()
    leistung = forms.IntegerField()
    artikelnummer = forms.CharField(max_length=100)
    zulieferer = forms.CharField(max_length=100)
    preis_ek = forms.CharField(max_length=100)
    preis_vk = forms.CharField(max_length=100)
    lagerort = forms.CharField(max_length=100)
