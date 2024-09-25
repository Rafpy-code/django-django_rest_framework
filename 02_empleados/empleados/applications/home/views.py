from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import PruebaBBDD
from .forms import PruebaForm

# Create your views here.

# Vista de la página de inicio
class HomePageView(TemplateView):
    template_name = 'home/home.html'

# Esto era para las pruebas
# class HomeView(TemplateView):
#     # /home porque ahora están dentro de la carpeta templates 
#     template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['a', 'b', 'c']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = PruebaBBDD
    template_name = "home/lista_prueba.html"
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    model = PruebaBBDD
    template_name = "home/add.html"
    # fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/lista_prueba'
