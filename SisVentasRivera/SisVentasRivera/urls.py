from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('SisVentasRivera.Apps.ventas.urls')),    
    url(r'^$','django.contrib.auth.views.login',{'template_name':'Principal/index.html'},name="login"),
	url(r'^$','django.contrib.auth.views.logout_then_login',name="salir"),
	url(r'^accounts/', include('registration.urls')),
)
