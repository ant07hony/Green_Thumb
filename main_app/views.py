from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gardens_index(request):
    gardens = Garden.objects.all()
    return render(request, 'gardens/index.html',{
        'gardens': gardens
    })

def journal(request, garden_id):
    garden = Garden.objects.get(id=garden_id)
    return render(request, 'gardens/journal.html', {
       'garden': garden 
    })
    

class GardenCreate(CreateView):
    model = Garden
    fields = ['name', 'description', 'date', 'journal']
    
class GardenUpdate(UpdateView):
    model = Garden
    fields = ['description', 'date', 'journal']

class GardenDelete(DeleteView):
    model = Garden
    success_url = '/gardens'
    