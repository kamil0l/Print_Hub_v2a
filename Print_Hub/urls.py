"""
URL configuration for HUB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hub import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name= 'index'),
    path('printing/', views.PrintingListView.as_view(), name= 'printing_list'),
    path('printer/', views.PrinterListView.as_view(), name= 'printer_list'),
    path('addPrinter/', views.AddPrinter.as_view(), name= 'add_printer'),
    path('project/', views.ProjectListView.as_view(), name= 'project'),
    path('addProject/', views.AddProject.as_view(), name= 'add_project'),
    path('filament/', views.FilamentListView.as_view(), name= 'filament'),
    path('addFilament/', views.AddFilament.as_view(), name= 'add_filament'),


]
