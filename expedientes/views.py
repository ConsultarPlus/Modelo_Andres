from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, CreateView
from . import models
from .models import Expedientes
from .forms import ExpedienteForm
from django.contrib import messages
from .filters import ExpedientesFilter
from django.urls import reverse
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class ExpedientesList(ListView):
    model = models.Expedientes
    template_name = 'Expedientes_list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order = self.request.GET.get('orderby', 'id')
        object_list = Expedientes.objects.filter(
            observacion=filter_val,
        ).order_by(order)
        return object_list


def expediente_dsp_view(request, pk):
    id_expediente = Expedientes.objects.get(pk=pk)
    context = {
        'form': id_expediente
    }
    return render(request, 'Expediente_Dsp.html', context)


def expediente_baja_view(request, pk):
    # exp = Expedientes.objects.get(pk=pk)
    exp = Expedientes.objects.get(pk=pk)
    if request.method == 'POST':
        exp.delete()

    context = {
        'form': exp
    }
    return render(request, 'Expediente_Baja.html', context)


import datetime
from django.contrib.auth.models import User


class ExpedienteCreateView(CreateView):
    models = models.Expedientes
    template_name = 'Expediente_Alta.html'
    form_class = ExpedienteForm
    success_url = '/expedientes'
    initial = {
        'fecha_inicio': datetime.date.today()
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_carga = self.request.user
        self.object.save()
        return super(ExpedienteCreateView, self).form_valid(form)


def expediente_alta_view(request):
    form = ExpedienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ExpedienteForm()

    context = {
        'form': form
    }
    return render(request, 'Expediente_Alta.html', context)


def expediente_upd_view(request, pk):
    obj = get_object_or_404(Expedientes, id=pk)
    form = ExpedienteForm(request.POST or None, instance=obj)

    context = {'form': form}
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, "El expediente se ha modificado con éxito.")
        context = {'form': form}
        return render(request, 'Expediente_Upd.html', context)
    else:
        context = {'form': form,
                   'error': 'Se ha producido un error, los datos no han sido modificados'}
        return render(request, 'Expediente_Upd.html', context)


def search(request):
    expedientes_list = Expedientes.objects.all()
    expedientes_filter = ExpedientesFilter(request.GET, queryset=expedientes_list)
    return render(request, 'Expedientes_list.html', {'filter': expedientes_filter})
