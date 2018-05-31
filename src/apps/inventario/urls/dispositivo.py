from django.conf.urls import url
from apps.inventario import views as inventario_v

urlpatterns = [
    # Listado de Teclados
    url(
        r'^teclado/(?P<triage>[\w\d-]+)/edit/$',
        inventario_v.TecladoUpdateView.as_view(),
        name='teclado_update'
        ),
    # Detalle de cada teclado
    url(
        r'^teclado/(?P<triage>[\w\d-]+)/$',
        inventario_v.TecladoDetailView.as_view(),
        name='teclado_detail'
        ),
    # Creación de fallas de dispositivos
    url(
        r'^falla/add/$',
        inventario_v.DispositivoFallaCreateView.as_view(),
        name='dispositivofalla_add'
    ),
    #  Detalles de cada monitor
    url(
        r'^monitor/(?P<triage>[\w\d-]+)/$',
        inventario_v.MonitorDetailView.as_view(),
        name='monitor_detail'
        )

]
