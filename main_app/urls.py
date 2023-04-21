from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    
    path('gardens/', views.gardens_index, name='index'),
    
    path('gardens/<int:garden_id>/', views.journal, name='journal'),
    
    path('gardens/create/', views.GardenCreate.as_view(), name='gardens_create'),
    
    path('gardens/<int:pk>/update/', views.GardenUpdate.as_view(), name='gardens_update'),
    
    path('gardens/<int:pk>/delete/', views.GardenDelete.as_view(), name='gardens_delete'),
    
    path('gardens/<int:garden_id>/add_plant/', views.add_plant, name='add_plant'),
    
    path('gardens/<int:pk>/update', views.PlantUpdate.as_view(), name='edit_plant'),
    
    path('gardens/<int:pk>/delete', views.PlantDelete.as_view(), name='delete_plant'),
]