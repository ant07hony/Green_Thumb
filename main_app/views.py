from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def gardens_index(request):
    gardens = Garden.objects.filter(user=request.user)
    return render(request, 'gardens/index.html',{
        'gardens': gardens
    })
@login_required
def journal(request, garden_id):
    garden = Garden.objects.get(id=garden_id)
    plant_form = PlantForm()
    return render(request, 'gardens/journal.html', {
       'garden': garden,
       'plant_form': plant_form,
    })
    

# def add_entry(request, garden_id):
#     form = JournalForm(request.POST)
#     if form.is_valid():
#         new_entry = form.save(commit=False)
#         new_entry.garden_id = garden_id
#         new_entry.save()
#     return redirect('journal', garden_id=garden_id)
    
@login_required
def add_plant(request, garden_id):
    form = PlantForm(request.POST)
    if form.is_valid():
        new_plant = form.save(commit=False)
        new_plant.garden_id = garden_id
        new_plant.save()
    return redirect('journal', garden_id=garden_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    

class GardenCreate(LoginRequiredMixin, CreateView):
    model = Garden
    fields = ['name', 'description', 'date', 'journal']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class GardenUpdate(LoginRequiredMixin, UpdateView):
    model = Garden
    fields = ['description', 'date', 'journal']

class GardenDelete(LoginRequiredMixin, DeleteView):
    model = Garden
    success_url = '/gardens'
    
class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['name','date','variety']
    success_url = '/gardens'

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/garden/<int:garden_id>'
    
class JournalList(ListView):
    model = Garden
    fields = ['date', 'journal']
    template_name = "gardens/journal.html"