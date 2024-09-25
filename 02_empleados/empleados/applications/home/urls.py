from django.urls import path
from django.contrib import admin

# from .views import HomeView
from . import views

app_name = 'home_app'

urlpatterns = [
    path('admin/', admin.site.urls),  # Esto incluye las URLs del admin
    # path('home/', views.HomeView.as_view()), # Esto era para las pruebas
    path('', views.HomePageView.as_view(), name='inicio'),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
]
