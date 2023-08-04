# w pliku forms.py
from django import forms
from .models import Filament, Printer, Parts

class FilamentForm(forms.ModelForm):
    class Meta:
        model = Filament
        fields = ('name', 'producer', 'material', 'colour', 'temperature_min', 'temperature_max', 'weight')

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ('name', 'head', 'max_temperature', 'max_speed', 'image')

class PartsForm(forms.ModelForm):
    printers = forms.ModelMultipleChoiceField(
        queryset=Printer.objects.all(),  # Pobierz dostępne drukarki
        widget=forms.CheckboxSelectMultiple,  # Użyj checkboxów
        label="Przypisz do drukarki",
        required=False  # Nie wymagaj wyboru
    )

    class Meta:
        model = Parts
        fields = ['name', 'description', 'printers']