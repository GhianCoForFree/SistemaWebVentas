from django.db import models
from django.contrib.auth.models import User

class Proveedor(models.Model):
	RUC = models.CharField(max_length=11)
	Razon_social = models.CharField(max_length=150)
	Direccion = models.CharField(max_length=200)	
	Telefono = models.CharField(max_length=6)
	Representante = models.CharField(max_length=150)
	Comentario = models.TextField()
	Estado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.Razon_social	

class Productos(models.Model):
	Nombre = models.CharField(max_length=150)
	Marca = models.CharField(max_length=100)
	PrecioconIGV = models.BooleanField(default=False)
	IGV = models.IntegerField(default=18)
	Stock = models.IntegerField()
	Imagen = models.ImageField(upload_to='SisVentasRivera/Static/media/Productos')
	Proveedor = models.ForeignKey(Proveedor)
	Precio = models.DecimalField(max_digits=9,decimal_places=2)
	Stock = models.IntegerField()
	Referencia = models.CharField(max_length=200)

	def __unicode__(self):
		return '%s, Marca: %s, Stock: %s ' % (self.Nombre,self.Marca,self.Stock)

class Factura_detalle(models.Model):
	Producto = models.ForeignKey(Productos)
	Cantidad = models.IntegerField()
	PrecioTransaccion = models.IntegerField()
	IGV = models.IntegerField()
	Subtotal = models.IntegerField()

##################################################################
##class Persona(models.Model):									##
##	Nombre = models.CharField(max_length=150)					##
##	Apellidos = models.CharField(max_length=150)				##
##	DNI = models.CharField(max_length=8)						##
##	Direccion = models.CharField(max_length=200)				##
##	Edad = models.IntegerField()								##
##																##
##	def __unicode__(self):										##
##		nombrecompleto = '%s %s' %(self.Nombre,self.Apellidos)	##
##		return nombrecompleto									##
##################################################################

class Empresa(models.Model):
	Razon_social = models.CharField(max_length=100)
	Sucursal = models.CharField(max_length=150)
	Direccion = models.CharField(max_length=150)
	Telefono = models.CharField(max_length=6)
	Representante = models.CharField(max_length=150)
	Cantidad_trabajadores = models.IntegerField()
	Estado = models.BooleanField(default=True)
	RUC = models.CharField(max_length=11)

	def __unicode__(self):
		return self.Razon_social

class Cargo_Emp(models.Model):
	Descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.Descripcion

class Usuario(models.Model):
	Nombre = models.CharField(max_length=150)
	Apellidos = models.CharField(max_length=150)
	Direccion = models.CharField(max_length=150)
	DNI = models.CharField(max_length=8)
	Fecha_nacimiento = models.DateField() 
	Foto = models.ImageField(upload_to='SisVentasRivera/Static/media/Usuarios',verbose_name="Foto")
	Telefono = models.CharField(max_length=6)
	Celular = models.CharField(max_length=9)
	E_mail = models.CharField(max_length=150)	
	Usuario = models.CharField(max_length=20)
	Contra = models.CharField(max_length=8)
	Estado = models.BooleanField(default=True)
	Cargo = models.ForeignKey(Cargo_Emp)	

	def __unicode__(self):
		return self.Usuario

class Cliente(models.Model):	
	Nombre = models.CharField(max_length=150)
	Apellidos = models.CharField(max_length=150)
	Razon_social = models.CharField(max_length=200)
	Direccion_legal=models.CharField(max_length=150, default='Piura')
	Direccion_entrega=models.CharField(max_length=150)
	Tipo = models.CharField(max_length=100)
	DNI = models.CharField(max_length=8)
	RUC = models.CharField(max_length=11)
	Telefono = models.CharField(max_length=9)
	E_mail = models.CharField(max_length=150)
	Web = models.CharField(max_length=100)
	RUC = models.CharField(max_length=11)

	def __unicode__(self):
		nombrecompleto = '%s %s' % (self.Nombre,self.Apellidos)
		return nombrecompleto
#################################################################
#class Vendedor(models.Model):									#
#	Nombre = models.CharField(max_length=150)					#
#	Apellidos = models.CharField(max_length=150)				#
#	Comision = models.IntegerField()							#
#	Cargo = models.ForeignKey(Cargo_Emp)						#
#																#
#	def __unicode__(self):										#
#		nombrecompleto = '%s %s' % (self.Nombre,self.Apellidos) #
#		return nombrecompleto									#
#################################################################
class Factura_cabecera(models.Model):
	Sucursal = models.ForeignKey(Empresa)
	Fecha = models.DateField()
	Estado = models.BooleanField(default=True) 
	Cliente = models.ForeignKey(Cliente)
	Vendedor = models.ForeignKey(Usuario)

class Comentarios(models.Model):
	Usuario = models.ForeignKey(Usuario)
	timestamp = models.DateTimeField(auto_now_add=True)
	comentario = models.TextField()

	def __unicode__(self):
		return unicode(self.Usuario)


