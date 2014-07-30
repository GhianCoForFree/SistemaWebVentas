from django import forms
from django.forms import ModelForm
from models import *

class ProductoNuevo(ModelForm):
	class Meta:
		model = Productos
		exclude =('Imagen',)

class ProveedorNuevo(ModelForm):
	class Meta:
		model = Proveedor

class ClienteNuevo(ModelForm):
	class Meta:
		model = Cliente

class Comentario(ModelForm):
	class Meta:
		model = Comentarios