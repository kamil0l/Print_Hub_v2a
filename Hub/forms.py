# w pliku forms.py
from django import forms
from .models import Filament

class FilamentForm(forms.ModelForm):
    class Meta:
        model = Filament
        fields = ('name', 'producer', 'material', 'colour', 'temperature_min', 'temperature_max', 'weight')
