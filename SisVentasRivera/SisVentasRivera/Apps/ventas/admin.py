from django.contrib import admin
from SisVentasRivera.Apps.ventas.models import *

admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(Productos)
admin.site.register(Factura_detalle)
admin.site.register(Empresa)
admin.site.register(Cargo_Emp)
admin.site.register(Cliente)
admin.site.register(Factura_cabecera)
admin.site.register(Comentarios)