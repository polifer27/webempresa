from django.shortcuts import render
from .models import Service
# Create your views here.

#def services(request):
#    projects = Project.objects.all()

#    return render(request, "services/services.html")
def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html", {'services':services})   