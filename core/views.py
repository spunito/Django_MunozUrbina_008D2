from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Clientes, Productos_Animal
from .forms import ProductoForm ,ProductoForm2, clientesForm, clientesForm2
import os

# Create your views here.
TEMPLATES_DIRS=(
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")
def somos(request):
    return render(request ,"somos.html")
def galeria(request):
    return render(request ,"galeria.html")
def contacto(request):
    return render(request,"contacto.html")
def mapa(request):
    return render(request ,"maps.html")
def dogApi(request):
    return render(request,"dogsAPI.html")
def login(request):
    return render(request,"login.html")
def noCuenta(request):
    return render(request , "no_cuenta.html")

#Termino Templates normales - Inicia Templates CRUD

def mostrar(request):
    productos = Productos_Animal.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)

def form_producto(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrar')
    else:
        producto_form= ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})


def form_mod_producto(request, id): 
    producto = Productos_Animal.objects.get(id_producto=id)
    datos = {
        'form': ProductoForm2(instance=producto)
    }
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(producto.imagen) > 0:
                os.remove(producto.imagen.path)
        formulario = ProductoForm2(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar')
    return render (request, 'form_mod_producto.html', datos )

def form_del_producto(request, id):
    producto = Productos_Animal.objects.get(id_producto=id)
    producto.delete()
    return redirect('mostrar')


#CLIENTES
def mostrar1(request):
    cliente = Clientes.objects.all()
    datos = {
        'clientes': cliente
    }
    return render(request, 'mostrar_clientes.html', datos)

def form_clientes(request):
    if request.method=='POST': 
        clientes_form = clientesForm(request.POST)
        if clientes_form.is_valid():
            clientes_form.save()
            return redirect('index')
    else:
        clientes_form= clientesForm()
    return render(request, 'form_crear_clientes.html', {'clientes_form': clientes_form})


def form_mod_clientes(request, id): 
    cliente = Clientes.objects.get(rut_cliente=id)
    datos = {
        'form': clientesForm2(instance=cliente)
    }
    if request.method=='POST':
        formulario = clientesForm2(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar_clientes')
    return render (request, 'form_mod_clientes.html', datos )

def form_del_clientes(request, id):
    cliente = Clientes.objects.get(rut_cliente=id)
    cliente.delete()
    return redirect('mostrar_clientes')



