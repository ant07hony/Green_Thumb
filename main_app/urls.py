from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    
    path('gardens/', views.gardens_index, name='index'),
    
    path('gardens/<int:garden_id>/', views.journal, name='journal'),
]