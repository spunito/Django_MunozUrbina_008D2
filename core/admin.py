from django.contrib import admin
from .models import CategoriaAnimal, Clientes,Productos_Animal,SexoCliente
# Register your models here.

admin.site.register(CategoriaAnimal)
admin.site.register(Productos_Animal)

admin.site.register(SexoCliente)
admin.site.register(Clientes)

