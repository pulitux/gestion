from django.shortcuts import render
from empleados.models import Empleado


def buscaporoficio(request):
    empleado = Empleado()
    resultado = empleado.oficios()
    contexto = {
        'lista_oficios': resultado
    }
    return render(request, "buscaporoficio.html", contexto)

def buscapornombre(request):
    empleado = Empleado()
    cursor=empleado.nombres()
    contexto = {
        'lista_nombres': cursor
    }
    return render(request, "buscapornombre.html", contexto)

def muestraporoficio(request):
    ofi = request.POST['txtOficio']
    emple = Empleado()
    cursor=emple.buscaporoficio(ofi)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "muestrabusqueda.html", contexto)

def muestrapornombre(request):
    nombre = request.POST['txtNombre']
    emple = Empleado()
    cursor=emple.buscapornombre(nombre)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "muestrabusqueda.html", contexto)
