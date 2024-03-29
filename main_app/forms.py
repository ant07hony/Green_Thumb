from django.forms import ModelForm 
from .models import *

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name','date','variety']
        
class JournalForm(ModelForm):
    class Meta:
        model = Garden
        fields = ['date', 'journal']        
        