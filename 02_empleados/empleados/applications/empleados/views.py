from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Empleado
# Forms
from .forms import EmpleadoForm

from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect

# Login de usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class LoginUser(LoginView):
    template_name = 'empleados/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_app:inicio')
    

class LogoutUser(LoginRequiredMixin, TemplateView):
    template_name = 'empleados/logout.html'
    login_url = reverse_lazy('home_app:inicio')
    

# 1.- Listar todos los empleados de la empresa
class ListAllEmpleados(LoginRequiredMixin, ListView):
    template_name = 'empleados/list_all.html'
    model = Empleado
    paginate_by = 5
    ordering = 'names'
    context_object_name = 'empleados'

    def get_queryset(self) -> QuerySet[Any]:
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            # full_name__icontains = palabra_clave
            Q(names__icontains=palabra_clave) | Q(last_name__icontains=palabra_clave)
        )
        return lista

# ADMIN
class ListaEmpleadosAdmin(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 6
    ordering = 'names'
    context_object_name = 'empleados'


# 2.- Listar todos los empleados de un área de la empresa
class ListByAreaEmpleados(LoginRequiredMixin, ListView):
    '''Lista a los empleados de un área determinada'''
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'
    # queryset = Empleado.objects.filter(
    #     department__short_name = 'Fumanchis'
    # )

    # Uso en lugar de queryset sobreescribiendo la función
    def get_queryset(self) -> QuerySet[Any]:
        area = self.kwargs['short_name'].capitalize()
        lista = Empleado.objects.filter(
            department__short_name = area
        )
        return lista

# 3.- Listar empleados por trabajo desempeñado
class ListByTrabajo(LoginRequiredMixin, ListView):
    '''Lista a los empleados de un área determinada'''
    template_name = 'empleados/list_by_trabajo.html'
    context_object_name = 'empleados'

    def get_queryset(self) -> QuerySet[Any]:
        trabajo_nombre = self.kwargs['trabajo'].capitalize()
        print('trabajo_nombre:', trabajo_nombre)

        # Diccionario para mapear los nombres de trabajos con sus valores numéricos
        trabajo_map = {
            'Desarrollador': '0',
            'Diseñador': '1',
            'Tester': '2',
            'Analista': '3',
            'OTRO': '4'
        }

        # Obtener el valor numérico correspondiente al nombre del trabajo
        trabajo_valor = trabajo_map.get(trabajo_nombre, None)
        print('trabajo_valor', trabajo_valor)
        if trabajo_valor is None:
            return Empleado.objects.none()  # Si el trabajo no existe, retornar un queryset vacío
        lista = Empleado.objects.filter(
            job = trabajo_valor
        )
        return lista
    

# 4.- Listar los empleados por palabra clave
class ListEmpleadosByKword(LoginRequiredMixin, ListView):
    '''Lista a los empleados por palabra clave'''
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self) -> QuerySet[Any]:
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            names = palabra_clave.capitalize()
        )
        print('queryset:', lista)
        return lista

# 5.- Listar habilidades de un empleado
class ListHabilidadesEmpleado(LoginRequiredMixin, ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self) -> QuerySet[Any]:
        identificador = self.request.GET.get('id', '')
        # Inicializar el atributo self.empleado como None
        self.empleado = None
        # Verificar si el campo id está vacío o no es un número válido
        if not identificador or not identificador.isdigit():
            return []  # No buscar si el id no es válido o está vacío

        try:
            empleado = Empleado.objects.get(id=identificador)
            self.empleado = empleado  # Guardar empleado para usar en el contexto
            return empleado.skills.all()  # Devolver habilidades del empleado
        except Empleado.DoesNotExist:
            self.empleado = None
            return []  # Si el empleado no existe, retornar un queryset vacío

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el empleado al contexto
        context['empleado'] = self.empleado
        return context
    
# DeatilView
class EmpleadoDetailView(LoginRequiredMixin, DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # Agregar el empleado al contexto
        context['title'] = 'Detalle del empleado'
        # context['empleado'] = self.object # model = Empleado arriba
        # Obtener las habilidades del empleado actual (self.object es el empleado)
        context['skills'] = self.object.skills.all()
        return context
    

class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = "empleados/succes.html"


class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    # fields = ['names', 'last_name', 'job', 'department', 'image', 'skills']
    # fields = ('__all__')
    form_class = EmpleadoForm
    # success_url = '/success'
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        # Logica adicional
        empleado = form.save(commit=False)
        empleado.full_name = empleado.names + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    

class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    # fields = [
    #     'names', 
    #     'last_name', 
    #     'job', 
    #     'department', 
    #     'image',
    #     'skills']
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Trae toda la información del formulario
        print('======================')
        print(request.POST)
        print('======================')
        print(request.POST['last_name'])
        print('======================')

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Logica adicional
        empleado = form.save(commit=False)
        empleado.full_name = empleado.names + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleados_app:empleados_admin')
    context_object_name = 'empleado'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el empleado al contexto
        context['title'] = 'Empleado eliminado'
        return context
    