from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import PlantForm

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
    plant_form = PlantForm()
    return render(request, 'gardens/journal.html', {
       'garden': garden,
       'plant_form': plant_form,
    })
    
def add_plant(request, garden_id):
    form = PlantForm(request.POST)
    if form.is_valid():
        new_plant = form.save(commit=False)
        new_plant.garden_id = garden_id
        new_plant.save()
    return redirect('journal', garden_id=garden_id)
    

class GardenCreate(CreateView):
    model = Garden
    fields = ['name', 'description', 'date', 'journal']
    
class GardenUpdate(UpdateView):
    model = Garden
    fields = ['description', 'date', 'journal']

class GardenDelete(DeleteView):
    model = Garden
    success_url = '/gardens'
    