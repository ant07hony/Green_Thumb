from django.shortcuts import render
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