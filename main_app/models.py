from django.db import models

# Create your models here.
class Garden(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    journal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name