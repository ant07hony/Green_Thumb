from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

LIGHT = (
    ('S', 'Full Sun'),
    ('PS', 'Partial Sun'),
    ('FS', 'Full Shade'),
)

# Create your models here.
class Garden(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField()
    date = models.DateField()
    journal = models.TextField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('journal', kwargs={'garden_id': self.id})
    
    
class Care_Guide(models.Model):
    zone = models.CharField()
    food = models.CharField(max_length=100)
    light = models.CharField(choices=LIGHT, default=LIGHT[0][0])
    water = models.CharField()
    companions = models.CharField()
    notes = models.CharField()
    
    
    def __str__(self):
        return self.name
    
    
    
class Plant(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    variety = models.CharField(max_length=100)
    seeds_sown = models.IntegerField(null=True)
    germination = models.DateField(null=True)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.get_variety_display()} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('journal', kwargs={'garden_id': self.id})
    
    class Meta:
        ordering = ['-date']