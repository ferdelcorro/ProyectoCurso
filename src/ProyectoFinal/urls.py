from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProyectoFinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}
    ),

    url(r'^$', 'apps.veterinarian.views.index'),
    url(r'^signup/$', 'apps.veterinarian.views.sign_up'),

    url(r'^cargar_cliente/$', 'apps.client.views.cargar_cliente'),
    url(r'^buscar_cliente/$', 
            'apps.client.views.buscar_cliente'),
    url(r'^buscar_cliente/(?P<nombre>[a-zA-Z@.-_]+)/$', 
            'apps.client.views.buscar_cliente'),
    url(r'^mostrar_cliente/(?P<pk>\d+)/$', 
            'apps.client.views.mostrar_cliente',
            name='mostrar_cliente'),

    url(r'^cargar_mascota/$', 'apps.mascot.views.cargar_mascota'),
    url(r'^cargar_mascota/(?P<pk>\d+)/$', 
            'apps.mascot.views.cargar_mascota',
            name='cargar_mascota'),
    url(r'^mostrar_mascota/(?P<pk>\d+)/$', 
            'apps.mascot.views.mostrar_mascota',
            name='mostrar_mascota'),

    url(r'^cargar_historial/$', 
            'apps.clinic_history.views.cargar_historial',
            name='cargar_historial'),
    url(r'^cargar_historial/(?P<pk>\d+)/$', 
            'apps.clinic_history.views.cargar_historial',
            name='cargar_historial'),
    url(r'^historial/(?P<pk>\d+)/$', 
            'apps.clinic_history.views.historiales',
            name='historial'),
)
