from django.urls import path
from depts import views

urlpatterns = [
    path('', views.form, name='for'),
    path('form', views.form, name='form'),
    ]