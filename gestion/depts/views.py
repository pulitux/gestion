from django.shortcuts import render
from depts.models import Departamento


def lista(request):
    dept = Departamento()
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'dept_index.html', contexto)

def alta(request):
    dept = Departamento()
    contexto = dept.tablaDepartamentos()
    print(contexto)

    return render(request, 'dept_alta.html', contexto)

def add(request):
    dept = Departamento()
    dept.add(request)
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'dept_index.html', contexto)

def baja(request):
    dept = Departamento()
    contexto = dept.tablaDepartamentos()

    return render(request, 'dept_baja.html', contexto)

def delete(request):
    dept = Departamento()
    dept.delete(request)
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'dept_index.html', contexto)

def modificar(request):
    dept = Departamento()
    contexto = dept.tablaDepartamentos()

    return render(request,'dept_modificar.html', contexto)

def modify(request):
    dept = Departamento()
    dept.modify(request)
    cursor = dept.listaDepartamentos()
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'dept_index.html', contexto)

def search(request):
    dept = Departamento()
    cursor = dept.search(request)
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'dept_index.html', contexto)
