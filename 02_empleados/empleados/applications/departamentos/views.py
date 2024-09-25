from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import NewDepartmentForm
from .models import Departamento
from applications.empleados.models import Empleado

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class DepartamentoListView(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = "departamentos/lista.html"
    context_object_name = 'departamentos'
    ordering = 'name'
    

class NewDepartmentView(LoginRequiredMixin, FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartmentForm
    success_url = reverse_lazy('departamentos_app:departamento_list')

    def form_valid(self, form):
        # Creo una instancia de Departamento
        departamento = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['nombre_corto']
        )
        departamento.save()
        print(departamento)
        

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            names=nombre,
            last_name=apellidos,
            job='1',
            department=departamento
        )
        
        return super(NewDepartmentView,self).form_valid(form)