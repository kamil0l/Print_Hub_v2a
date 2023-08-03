from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .forms import FilamentForm, PrinterForm
from .models import Filament, Printer

class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')

class PrintingList(View):

    def get(self, request):
        """printings = Printing.objects.all()"""
        return render(request, 'printing_list.html' )

class PrinterList(View):

    def get(self, request):
        printers = Printer.objects.all()
        return render(request, 'printer_list.html', {'printers': printers})

class AddPrinter(View):

    def get(self, request):
        form = PrinterForm()
        return render(request, 'add_printer.html', {'form': form})

    def post(self, request):
        form = PrinterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('printer_list')
        return render(request, 'add_printer.html', {'form': form})


class DeletePrinter(View):
    def post(self, request, printer_id):
        printer = Printer.objects.get(id=printer_id)
        printer.delete()
        return redirect('printer_list')

class EditPrinter(View):

    def get(self, request, printer_id):
        printer = get_object_or_404(Printer, id=printer_id)
        form = PrinterForm(instance=printer)
        return render(request, 'edit_printer.html', {'form': form, 'printer': printer})

    def post(self, request, printer_id):
        printer = get_object_or_404(Printer, id=printer_id)
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            return redirect('printer_list')
        return render(request, 'edit_printer.html', {'form': form, 'printer': printer})


class ProjectList(View):

    def get(self, request):
        """projects = Project.objects.all()"""
        return render(request, 'project_list.html')

class AddProject(View):

    def get(self, request):
        """form = AddProjectForm()"""
        return render(request, 'add_project.html')

class FilamentList(View):

    def get(self, request):
        filaments = Filament.objects.all()
        return render(request, 'filament_list.html', {'filaments': filaments})

class AddFilament(View):
    def get(self, request):
        form = FilamentForm()
        return render(request, 'add_filament.html', {'form': form})

    def post(self, request):
        form = FilamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filament')
        return render(request, 'add_filament.html', {'form': form})

class PartsList(View):
    def get(self, request):
        """parts = Parts.object.all()"""
        return render(request, 'parts.html')

class AddParts(View):
    def get(self, request):
        """form = AddPartsForm()"""
        return render(request, 'add_parts.html')

class DeleteFilament(View):
    def post(self, request, filament_id):
        filament = Filament.objects.get(id=filament_id)
        filament.delete()
        return redirect('filament')

class EditFilament(View):
    def get(self, request, filament_id):
        filament = get_object_or_404(Filament, id=filament_id)
        form = FilamentForm(instance=filament)
        return render(request, 'edit_filament.html', {'form': form, 'filament': filament})

    def post(self, request, filament_id):
        filament = get_object_or_404(Filament, id=filament_id)
        form = FilamentForm(request.POST, instance=filament)
        if form.is_valid():
            form.save()
            return redirect('filament')
        return render(request, 'edit_filament.html', {'form': form, 'filament': filament})


