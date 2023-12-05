from django.urls import path
from empleados import views

urlpatterns = [
    #path('', views.lista, name='lista'),
    #path('nuevo', views.nuevo, name='nuevo'),
    path('buscaporoficio', views.buscaporoficio, name='buscaporoficio'),
    path('buscapornombre', views.buscapornombre, name='buscapornombre'),
    path('muestraporoficio', views.muestraporoficio, name='muestraporoficio'),
    path ('muestrapornombre', views.muestrapornombre, name ='muestrapornombre')
]