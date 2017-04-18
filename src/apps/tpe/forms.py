from django import forms
from django.forms import ModelForm
from django.db.models import Count

from apps.users.models import Perfil
from apps.tpe.models import Equipamiento, Garantia, TicketSoporte, TicketRegistro, Monitoreo, TicketReparacion
from apps.mye.models import Cooperante, Proyecto
from apps.escuela.forms import EscuelaBuscarForm


class EquipamientoNuevoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento
        fields = ('id', 'escuela')
        labels = {
            'id': 'Número de entrega'}
        widgets = {
            'id': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'escuela': forms.HiddenInput()}


class EquipamientoForm(ModelForm):
    class Meta:
        model = Equipamiento
        fields = '__all__'
        exclude = ('id',)
        widgets = {
            'escuela': forms.HiddenInput(),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            'cooperante': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'proyecto': forms.SelectMultiple(attrs={'class': 'form-control select2'})}


class GarantiaForm(forms.ModelForm):
    class Meta:
        model = Garantia
        fields = '__all__'
        widgets = {
            'equipamiento': forms.Select(attrs={'class': 'form-control select2'}),
            'fecha_vencimiento': forms.TextInput(attrs={'class': 'form-control datepicker'})
        }

    def __init__(self, *args, **kwargs):
        super(GarantiaForm, self).__init__(*args, **kwargs)
        self.fields['equipamiento'].queryset = self.fields['equipamiento'].queryset.annotate(num_garantias=Count('garantias')).filter(num_garantias__lt=1)


class TicketSoporteForm(forms.ModelForm):
    class Meta:
        model = TicketSoporte
        fields = ('garantia', 'descripcion',)
        widgets = {
            'garantia': forms.HiddenInput(),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }


class TicketCierreForm(forms.ModelForm):
    class Meta:
        model = TicketSoporte
        fields = ('cerrado',)
        widgets = {
            'cerrado': forms.HiddenInput()
        }


class TicketRegistroForm(forms.ModelForm):
    class Meta:
        model = TicketRegistro
        fields = ('tipo', 'descripcion', 'foto')
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.URLInput(attrs={'class': 'form-control'}),
        }


class TicketReparacionForm(forms.ModelForm):
    class Meta:
        model = TicketReparacion
        fields = ('triage', 'tipo_dispositivo', 'falla_reportada', 'tecnico_asignado')


class TicketReparacionListForm(forms.ModelForm):
    class Meta:
        model = TicketReparacion
        fields = ('estado', 'tecnico_asignado')

    def __init__(self, *args, **kwargs):
        super(TicketReparacionListForm, self).__init__(*args, **kwargs)
        self.fields['estado'].required = False
        self.fields['tecnico_asignado'].queryset = Perfil.objects.filter(user__in=TicketReparacion.objects.values('tecnico_asignado').distinct())
        self.fields['tecnico_asignado'].required = False


class TicketReparacionUpdateForm(forms.ModelForm):
    class Meta:
        model = TicketReparacion
        fields = ('falla_encontrada', 'solucion_tipo', 'solucion_detalle')
        widgets = {
            'falla_encontrada': forms.Textarea(attrs={'class': 'form-control'}),
            'solucion_tipo': forms.Select(attrs={'class': 'form-control'}),
            'solucion_detalle': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EquipamientoListForm(EscuelaBuscarForm):
    nombre = forms.CharField(
        widget=forms.TextInput(),
        required=False)
    fecha_min = forms.CharField(
        label='Fecha mínima',
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
        required=False)
    fecha_max = forms.CharField(
        label='Fecha máxima',
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
        required=False)
    cooperante_tpe = forms.ModelChoiceField(
        label='Cooperante de equipamiento',
        queryset=Cooperante.objects.all(),
        required=False)
    proyecto_tpe = forms.ModelChoiceField(
        label='Proyecto de equipamiento',
        queryset=Proyecto.objects.all(),
        required=False)

    def __init__(self, *args, **kwargs):
        super(EquipamientoListForm, self).__init__(*args, **kwargs)
        self.fields.pop('sector')
        self.fields.pop('cooperante_mye')
        self.fields.pop('proyecto_mye')
        self.fields.pop('poblacion_min')
        self.fields.pop('poblacion_max')
        self.fields.pop('solicitud')
        self.fields.pop('solicitud_id')
        self.fields.pop('equipamiento')


class MonitoreoListForm(forms.Form):
    usuario = forms.ModelChoiceField(
        label='Usuario',
        required=False,
        queryset=Perfil.objects.filter(user__in=Monitoreo.objects.values('creado_por').distinct()))
    fecha_min = forms.CharField(
        label='Fecha mínima',
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
        required=False)
    fecha_max = forms.CharField(
        label='Fecha máxima',
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
        required=False)
