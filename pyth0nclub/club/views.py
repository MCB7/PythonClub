from django.shortcuts import render
from .models import Resource, Meeting, Event

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def resource(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html',{'resource_list': resource_list})
    