from django.shortcuts import reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView,  UpdateView, DetailView, FormView
from django.db.models import Sum
from braces.views import (
    LoginRequiredMixin
)
from apps.inventario import models as inv_m
from apps.inventario import forms as inv_f


class EntradaCreateView(LoginRequiredMixin, CreateView):
    """Vista   para obtener los datos de Entrada mediante una :class:`entrada`
    Funciona  para recibir los datos de un  'EntradaForm' mediante el metodo  POST.  y
    nos muestra el template de visitas mediante el metodo GET.
    """

    model = inv_m.Entrada
    form_class = inv_f.EntradaForm
    template_name = 'inventario/entrada/entrada_add.html'

    def form_valid(self, form):
        form.instance.creada_por = self.request.user
        form.instance.recibida_por = self.request.user
        return super(EntradaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EntradaCreateView, self).get_context_data(**kwargs)
        context['listado'] = inv_m.Entrada.objects.filter(en_creacion='True')
        return context


class EntradaDetailView(LoginRequiredMixin, DetailView):
    """Para generar detalles de la :class:`entrada`   con sus respectivos campos.
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/entrada_detail.html'


class EntradaListView(LoginRequiredMixin, FormView):
    """Vista Encargada para mostrar las Lista de la :class:'Entrada' con su respectivo
    formulario de busqueda de filtros
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/entrada_list.html'
    form_class = inv_f.EntradaInformeForm


class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para actualizar de :class:`Entrada`. con sus respectivos campos
    """
    model = inv_m.Entrada
    form_class = inv_f.EntradaUpdateForm
    template_name = 'inventario/entrada/entrada_edit.html'

    def get_success_url(self):
        return reverse('entrada_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(EntradaUpdateView, self).get_context_data(**kwargs)
        context['EntradaDetalleForm'] = inv_f.EntradaDetalleForm(initial={'entrada': self.object})
        return context


class EntradaDetalleView(LoginRequiredMixin, CreateView):
    """Vista   para obtener los datos de los Detalles de Entrada mediante una :class:`EntradaDetalle`
    Funciona  para recibir los datos de un  'EntradaDetalleForm' mediante el metodo  POST.  y
    nos muestra el template de visitas mediante el metodo GET.
    """
    model = inv_m.EntradaDetalle
    form_class = inv_f.EntradaDetalleForm
    template_name = 'inventario/entrada/entradadetalle_add.html'


class EntradaDetalleUpdateView(LoginRequiredMixin, UpdateView):
    """Vista Encargada de actualizar los datos mediante la :class:`EntradaDetalle`.
    """
    model = inv_m.EntradaDetalle
    form_class = inv_f.EntradaDetalleUpdateForm
    template_name = 'inventario/entrada/entradadetalle_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntradaDetalleUpdateView, self).get_context_data(**kwargs)
        context['datos'] = inv_m.EntradaDetalle.objects.get(id=self.object.id)
        return context

    def get_initial(self):
        initial = super(EntradaDetalleUpdateView, self).get_initial()
        initial['creado_por'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse('entrada_update', kwargs={'pk': self.object.entrada.id})


class CartaAgradecimiento(LoginRequiredMixin, DetailView):
    """Muestra la carta agradecimiento
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/carta_agradecimiento.html'

    def get_context_data(self, **kwargs):
        context = super(CartaAgradecimiento, self).get_context_data(**kwargs)
        context['dispositivotipo_list'] = inv_m.EntradaDetalle.objects.filter(entrada=self.object.id)
        return context


class ConstanciaEntrada(LoginRequiredMixin, DetailView):
    """Muestra informe de la entrada en sucio
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/informe_sucio.html'

    def get_context_data(self, **kwargs):
        context = super(ConstanciaEntrada, self).get_context_data(**kwargs)
        context['dispositivotipo_list'] = inv_m.EntradaDetalle.objects.filter(entrada=self.object.id)
        tipo_dispositivo = inv_m.EntradaDetalle.objects.filter(
            entrada=self.object.id).values('tipo_dispositivo').distinct()
        lista = []
        util = []
        total = []
        contador = 0
        for tipo in tipo_dispositivo:
            acumulado_util = 0
            dispositivo_tipo = inv_m.EntradaDetalle.objects.filter(
                entrada=self.object.id,
                tipo_dispositivo=tipo['tipo_dispositivo']
                )
            contador = contador + 1
            for datos in dispositivo_tipo:
                acumulado_util = acumulado_util + datos.total
            nuevo_dispositivo = inv_m.DispositivoTipo.objects.get(id=tipo['tipo_dispositivo'])
            suma_util = inv_m.EntradaDetalle.objects.filter(
                                                            entrada=self.object.id,
                                                            tipo_dispositivo=tipo['tipo_dispositivo']).aggregate(
                                                            total_util=Sum('util')
                                                            )
            suma_repuesto = inv_m.EntradaDetalle.objects.filter(
                entrada=self.object.id,
                tipo_dispositivo=tipo['tipo_dispositivo']).aggregate(total_repuesto=Sum('repuesto'))
            suma_desecho = inv_m.EntradaDetalle.objects.filter(
                entrada=self.object.id,
                tipo_dispositivo=tipo['tipo_dispositivo']).aggregate(total_desecho=Sum('desecho'))
            suma_total = inv_m.EntradaDetalle.objects.filter(
                entrada=self.object.id,
                tipo_dispositivo=tipo['tipo_dispositivo']).aggregate(total_cantidad=Sum('total'))
            index = contador % 2
            diccionario = {
                'tipo_dipositivo': nuevo_dispositivo,
                'util': suma_util,
                'repuesto': suma_repuesto,
                'desecho': suma_desecho,
                'total': suma_total,
                'index': index}
            util.append(suma_util)
            lista.append(diccionario)
            total.append(acumulado_util)
        context['dispositivo_tipo'] = lista
        context['suma_util'] = util
        context['suma_total'] = total
        return context

                
class ImprimirQr(LoginRequiredMixin, DetailView):
    """
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/imprimir_qr.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs['detalle'])
        context = super(ImprimirQr, self).get_context_data(**kwargs)
        context['dispositivo_qr'] = inv_m.Dispositivo.objects.filter(entrada=self.object.id,
                                                                     entrada_detalle=self.kwargs['detalle'])
        return context


class ReporteRepuestosQr(LoginRequiredMixin, DetailView):
    """
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/imprimir_qr.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs['detalle'])
        context = super(ReporteRepuestosQr, self).get_context_data(**kwargs)
        context['dispositivo_qr'] = inv_m.Repuesto.objects.filter(entrada=self.object.id,
                                                                  entrada_detalle=self.kwargs['detalle'])
        return context


class EntradaDetalleDispositivos(LoginRequiredMixin, DetailView):
    """
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/entradadetalle_dispositivos.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs['detalle'])
        context = super(EntradaDetalleDispositivos, self).get_context_data(**kwargs)
        context['dispositivo_qr'] = inv_m.Dispositivo.objects.filter(entrada=self.object.id,
                                                                     entrada_detalle=self.kwargs['detalle'])
        return context


class EntradaDetalleRepuesto(LoginRequiredMixin, DetailView):
    """
    """
    model = inv_m.Entrada
    template_name = 'inventario/entrada/entradadetalle_repuesto.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs['detalle'])
        context = super(EntradaDetalleRepuesto, self).get_context_data(**kwargs)
        context['repuesto_qr'] = inv_m.Repuesto.objects.filter(entrada=self.object.id,
                                                               entrada_detalle=self.kwargs['detalle'])
        return context


class EntradaDescuentoCreateView(LoginRequiredMixin, CreateView):
    """
    """
    model = inv_m.DescuentoEntrada
    template_name = 'inventario/entrada/descuento_add.html'


class EntradaDescuentoDetailView(LoginRequiredMixin, DetailView):
    """docstring forEntradaDescuentoDetailView."""
    model = inv_m.DescuentoEntrada
    template_name = 'inventario/entrada/descuento_detail.html'


class EntradaDescuentoUpdateView(LoginRequiredMixin, UpdateView):
    """
    """
    model = inv_m.DescuentoEntrada
    template_name = 'inventario/entrada/descuento_update.html'
