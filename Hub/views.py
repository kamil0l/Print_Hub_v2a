from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')

class PrintingListView(View):

    def get(self, request):
        printings = Printing.objects.all()
        return render(request, 'printing_list.html')

class PrinterListView(View):

    def get(self, request):
        printers = Printer.objects.all()
        return render(request, 'printer_list.html')

class AddPrinter(View):

    def get(self, request):
        form = AddPrinterForm()
        return render(request, 'add_printer.html')


class ProjectListView(View):

    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'project_list.html')

class AddProject(View):

    def get(self, request):
        form = AddProjectForm()
        return render(request, 'add_project.html')

class FilamentListView(View):

    def get(self, request):
        filaments = Filament.object.all()
        return render(request, 'filament_liest.html')

class AddFilament(View):
    def get(self, request):
        form = AddFilamentForm()
        return render(request, 'add_filament.html')




