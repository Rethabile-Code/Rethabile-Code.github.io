from django.shortcuts import render
from .models import Projects
from App.models import Project
F


# Create your views here.
def home(request):
    return render(request,'index.html')

def add(request):
    if request.method == 'POST':
        if request.POST.get('Project_Name').request.POST.get('Upload_by').request.POST.get('dated')
            savest=Projects()
            savest.Porject_Name=request.POST.get('Project_Name')
            savest.Upload_by=request.POST.get('Upload_by')
            savest.Porject_Name=request.POST.get('dated')
            savest.save()
            messages.success(request,'The Record'+savest.Porject_Name+"is added successful")
            return render(request, 'index.html')
        else
            return render(request, 'index.html')