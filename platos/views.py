from django.shortcuts import render, redirect
from .models import Plato


# HOME
def home(request):
    return render(request,'platos/home.html')

# LISTADO
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'platos/lista.html', {'platos': platos})

# CREAR
def crear_plato(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']

        Plato.objects.create(nombre=nombre, precio=precio, descripcion=descripcion)
        return redirect('lista_platos')

    return render(request, 'platos/crear.html')

# ELIMINAR
def eliminar_plato(request, id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return redirect('lista_platos')