from django.urls import path
# from .views import HomeView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'empleados_app'

urlpatterns = [
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login'
        ),
    path('logout/', 
         LogoutView.as_view(next_page='home_app:inicio'), 
         name='logout'),

    path(
        'listar-todos-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
        ),
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path(
        'listar-por-area/<short_name>/', 
        views.ListByAreaEmpleados.as_view(),
        name='empleados_area'
        ),
    path(
        'listar-por-trabajo/<trabajo>/', 
        views.ListByTrabajo.as_view()
        ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadosByKword.as_view()
        ),
    path(
        'listar-habilidades-empleado/', 
        views.ListHabilidadesEmpleado.as_view()
        ),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
        ),
    path(
        'crear-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
        ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
        ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
        ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
        ),
]
