from django.shortcuts import render
from depts.models import Departamento


def lista(request):
    dept = Departamento()
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'index.html', contexto)

def alta(request):
    dept = Departamento()
    # cursor = dept.listaDepartamentos()
    # contexto = {
    #     'lista_departamentos': cursor
    # }
    contexto = dept.tablaDepartamentos()

    return render(request, 'alta.html', contexto)

def add(request):
    dept = Departamento()
    dept.add(request)
    contexto = dept.tablaDepartamentos()

    return render(request, 'index.html', contexto)

def baja(request):
    dept = Departamento()
    contexto = dept.tablaDepartamentos()

    return render(request, 'baja.html', contexto)

def delete(request):
    dept = Departamento()
    dept.delete(request)
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'index.html', contexto)

def modificar(request):
    dept = Departamento()
    contexto = dept.tablaDepartamentos()

    return render(request,'modificar.html', contexto)

def modify(request):
    dept = Departamento()
    dept.modify(request)
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'index.html', contexto)

def form(request):
    dept = Departamento()
    contexto = dept.tablaDepartamentos()
    return render(request, 'form.html', contexto)