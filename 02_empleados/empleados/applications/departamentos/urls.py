from django.urls import path
from . import views

# Nombre de la app para usar en el lista.html
app_name = 'departamentos_app'

urlpatterns = [
    path(
        'departamento_lista/',
        views.DepartamentoListView.as_view(),
        name='departamento_list'
    ),
    path(
        'new-departamento/',
        views.NewDepartmentView.as_view(),
        name='nuevo_departamento'
    ),
]