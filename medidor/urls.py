from django.urls import path
from . import views

urlpatterns = [
    path('contador/', views.contador_view, name='contador'),
    path('ver-datos/', views.ver_datos_agua, name='ver_datos'),
]
