from django.shortcuts import render
from depts.models import Departamento

def add(request):
    dept = Departamento()
    dept.add(request)

def delete(request):
    dept = Departamento()
    dept.delete(request)

def update(request):
    dept = Departamento()
    dept.modify(request)

def search(request):
    dept = Departamento()
    cursor = dept.search(request)
    contexto = {
        'lista_departamentos': cursor
    }
    return render(request, 'dept/search.html', contexto)
def form(request):
    dept = Departamento()
    action = request.POST['action'] if request.method == 'POST' else ''

    if action == 'add':
        dept.add(request)
    elif action == 'delete':
        dept.delete(request)
    elif action == 'update':
        dept.update(request)
    else:
        pass

    contexto = {
        'lista': dept.list(),
        'tabla': dept.table(),
    }
    return render(request, 'dept/form.html', contexto)
