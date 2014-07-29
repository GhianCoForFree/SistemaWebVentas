from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from models import *
from forms import *

def ProductoNew(request):	
	if request.method == "POST":
		formulario = ProductoNuevo(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/productos/agregar')
	else:
		formulario = ProductoNuevo()
	template = "Principal/ingresarproducto.html"
	return render_to_response(template,context_instance=RequestContext(request,locals()))		

def ProveedorNew(request):
	if request.method == "POST":
		formulario2 = ProveedorNuevo(request.POST)
		if formulario2.is_valid():
			formulario2.save()
			return HttpResponseRedirect('/proveedor/agregar')
	else:
		formulario2 = ProveedorNuevo()
	template = 'Principal/Ingresarproveedor.html'
	return render_to_response(template,context_instance=RequestContext(request,locals()))

def Registroventas(request):
	clientes = Cliente.objects.all()
	template = 'Principal/registroventa.html'
	return render_to_response(template,{'cliente':clientes}, context_instance=RequestContext(request))	

def Registrocliente(request):
	if request.method == "POST":
		formulario3 = ClienteNuevo(request.POST)
		if formulario3.is_valid():
			formulario3.save()
			return HttpResponseRedirect('/registro/venta')
	else:
		formulario3 = ClienteNuevo()
	template = 'Principal/registrocliente.html'
	return render_to_response(template,context_instance=RequestContext(request,locals()))

def Logeo(request):
	return render_to_response('Principal/index.html',context_instance=RequestContext(request))

def PanelAdmin(request):
	comentarios = Comentarios.objects.all()
	paginator = Paginator(comentarios,15)

	try: pagina = int(request.GET.get("page",'1'))
	
	except ValueError: pagina = 1

	try:
		comentarios = paginator.page(pagina)
	
	except (InvalidPage,EmptyPage):
		produc = paginator.page(paginator.num_pages)
	return render_to_response('Principal/panelAdministrador.html',{'comenta':comentarios},context_instance=RequestContext(request))

def PanelCajero(request):
	return render_to_response('Principal/panelCajero.html',context_instance=RequestContext(request))

def PanelVendedor(request):
	return render_to_response('Principal/panelVendedor.html',context_instance=RequestContext(request))
	
def gestion_Clientes(request):
	return render_to_response('Principal/gestionClientes.html',context_instance=RequestContext(request))

def listar_productos(request):
	produc = Productos.objects.all().order_by("-Precio")
	paginator = Paginator(produc,30)

	try: pagina = int(request.GET.get("page",'1'))
	
	except ValueError: pagina = 1

	try:
		produc = paginator.page(pagina)
	
	except (InvalidPage,EmptyPage):
		produc = paginator.page(paginator.num_pages)

	return render_to_response('Principal/listproductos.html',{'listar':produc},context_instance=RequestContext(request))

######################################################################################################################
##def crear_usuario(request):
##	if request.method=='POST':
##		formulario = UserCreationForm(request.POST)
##		if formulario.is_valid:
##			formulario.save()
##			return HttpRespondeRedirect('/')
##	else:
##		formulario = UserCreationForm()
##	return render_to_response('Principal/crearusuario.html',{'formulario':formulario},context_instance=RequestContext(request))		
##
##def ingresar(request):
##	if request.method=="POST":
##		formulario = AuthenticationForm(request.POST)
##		if formulario.is_valid:
##			usuario = request.POST['username']
##			clave = request.POST['password']
##			acceso = authenticate(username=usuario,password=clave)
##			if acceso is not None:
##				if acceso.is_active:
##					login(request, acceso)
##					return HttpRespondeRedirect('/privado')
##				else:
##					return render_to_response('noactivo.html',context_instance=RequestContext(request))
##			else:
##				return render_to_response('nousuario.html',context_instance=RequestContext(request))
##	else:
##		formulario = AuthenticationForm()
##	return render_to_response('login.html',{'formulario':formulario},context_instance=RequestContext(request))
######################################################################################################################