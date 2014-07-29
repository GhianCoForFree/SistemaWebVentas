from django.conf.urls import patterns, include, url

urlpatterns = patterns('SisVentasRivera.Apps.ventas.views',
	url(r'^$', 'Logeo', name='vista_login'),    
   #url(r'^usuario/nuevo$','crear_usuario', name='crear_usuario'),	
    url(r'^panel/admin$','PanelAdmin', name='panel_admin'),	
    url(r'^panel/cajero$', 'PanelCajero', name='panel_cajero'),	
    url(r'^panel/vendedor$', 'PanelVendedor', name='panel_vendedor'),	   
    url(r'^productos/ver$', 'listar_productos', name='panel_vendedor'),	   
    url(r'^Gestion/Clientes$', 'gestion_Clientes', name='gestion_Clientes'),    
    url(r'^productos/agregar$','ProductoNew', name='panel_admin'),	
    url(r'^proveedor/agregar$','ProveedorNew', name='ingresarproveedor'),	
    url(r'^registro/venta$','Registroventas', name='registroventa'),	   
    url(r'^registro/cliente$','Registrocliente', name='registrocliente'),      
)
