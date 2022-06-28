from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Productos_Animal,Clientes

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Productos_Animal
        fields = ['id_producto', 'descripcionP', 'marca', 'imagen','categoria']
        labels ={
            'id_producto': 'ID del producto', 
            'descripcionP' :'Descripcion Producto', 
            'marca': 'Marca', 
            'imagen':'Imagen',
            'categoria': 'Categoría',
        }
        widgets={
            'id_producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto',   
                }
            ), 
            'descripcionP': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'required': 'False',
                    'id': 'imagen'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

class ProductoForm2(forms.ModelForm):

    class Meta: 
        model= Productos_Animal
        fields = ['id_producto', 'descripcionP', 'marca', 'imagen','categoria']
        labels ={
            'id_producto': 'ID del producto', 
            'descripcionP' :'Descripcion Producto', 
            'marca': 'Marca', 
            'imagen':'Imagen',
            'categoria': 'Categoría',
        }
        widgets={
            'id_producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto',
                    'readonly':'readonly'
                }
            ), 
            'descripcionP': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'id': 'imagen'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }
 

 #CLIENTES

class clientesForm(forms.ModelForm):

    class Meta: 
        model= Clientes
        fields = ['rut_cliente', 'nombres_cliente', 'apellidos_clientes', 'correos_clientes','dirreciones_clientes','num_cel_clientes','sexo']
        labels ={
            'rut_cliente': 'rut del cliente', 
            'nombres_cliente' :'Nombres del cliente', 
            'apellidos_clientes': 'Apellidos cliente', 
            'correos_clientes':'Correo del cliente',
            'dirreciones_clientes': 'Direccion del cliente',
            'num_cel_clientes' : 'Numero celular cliente',
            'sexo' : 'sexo cliente',
        }
        widgets={
            'rut_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut_cliente',   
                }
            ), 
            'nombres_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombres', 
                    'id': 'nombres_cliente'
                }
            ), 
            'apellidos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellidos', 
                    'id': 'apellidos_clientes'
                }
            ), 
            'correos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo electronico', 
                    'id': 'correos_clientes'
                }
            ), 
            'dirreciones_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su dirrecion', 
                    'id': 'dirreciones_clientes'
                }
            ), 
            'num_cel_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su numero celular', 
                    'id': 'num_cel_clientes'
                }
            ), 
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'sexo'
                }
            ), 


        }

class clientesForm2(forms.ModelForm):

    class Meta: 
        model= Clientes
        fields = ['rut_cliente', 'nombres_cliente', 'apellidos_clientes', 'correos_clientes','dirreciones_clientes','num_cel_clientes','sexo']
        labels ={
            'rut_cliente': 'rut del cliente', 
            'nombres_cliente' :'Nombres del cliente', 
            'apellidos_clientes': 'Apellidos cliente', 
            'correos_clientes':'Correo del cliente',
            'dirreciones_clientes': 'Direccion del cliente',
            'num_cel_clientes' : 'Numero celular cliente',
            'sexo' : 'sexo cliente',
        }
        widgets={
            'rut_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut_cliente',  
                    'readonly':'readonly' 
                }
            ), 
            'nombres_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombres', 
                    'id': 'nombres_cliente'
                }
            ), 
            'apellidos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellidos', 
                    'id': 'apellidos_clientes'
                }
            ), 
            'correos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo electronico', 
                    'id': 'correos_clientes'
                }
            ), 
            'dirreciones_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su dirrecion', 
                    'id': 'dirreciones_clientes'
                }
            ), 
            'num_cel_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su numero celular', 
                    'id': 'num_cel_clientes'
                }
            ), 
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'sexo'
                }
            ), 

        }