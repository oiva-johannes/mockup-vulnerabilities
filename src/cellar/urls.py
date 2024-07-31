from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-inventory/', views.add_to_inventory, name='add_to_inventory')
]