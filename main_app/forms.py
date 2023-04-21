from django.forms import ModelForm 
from .models import *

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name','date','variety','seeds_sown','germination']
        
        
        name = models.CharField(max_length=100)
    date = models.DateField()
    variety = models.CharField(max_length=100)
    seeds_sown = models.IntegerField()
    germination = models.DateField()