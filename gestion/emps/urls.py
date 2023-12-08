from django.urls import path
from emps import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('index', views.lista, name='lista'),
    path('alta', views.alta, name='alta'),
    path('baja', views.baja, name='baja'),
    path('modificar', views.modificar, name='modificar'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('modify', views.modify, name='modify'),
    ]