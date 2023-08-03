# w pliku forms.py
from django import forms
from .models import Filament, Printer

class FilamentForm(forms.ModelForm):
    class Meta:
        model = Filament
        fields = ('name', 'producer', 'material', 'colour', 'temperature_min', 'temperature_max', 'weight')

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ('name', 'head', 'max_temperature', 'max_speed', 'image')