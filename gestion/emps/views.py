from django.shortcuts import render
from emps.models import Empleado


def lista(request):
    emp = Empleado()
    cursor = emp.listaEmpleados()
    contexto = {
        'lista_empleados': cursor
    }
    return render(request, 'emp_index.html', contexto)

def alta(request):
    emp = Empleado()
    contexto = emp.tablaEmpleados()
    return render(request, 'emp_alta.html', contexto)

def add(request):
    emp = Empleado()
    emp.add(request)
    cursor = emp.listaEmpleados()
    contexto = {
        'lista_empleados': cursor
    }
    return render(request, 'emp_index.html', contexto)

def baja(request):
    emp = Empleado()
    contexto = emp.tablaEmpleados()

    return render(request, 'emp_baja.html', contexto)

def delete(request):
    emp = Empleado()
    emp.delete(request)
    cursor = emp.listaEmpleados()
    contexto = {
        'lista_empleados': cursor
    }
    return render(request, 'emp_index.html', contexto)

def modificar(request):
    emp = Empleado()
    contexto = emp.tablaEmpleados()

    return render(request,'emp_modificar.html', contexto)

def modify(request):
    emp = Empleado()
    emp.modify(request)
    cursor = emp.listaEmpleados()
    contexto = {
        'lista_empleados': cursor
    }
    return render(request, 'emp_index.html', contexto)
