from django.contrib import admin
from .models import *
# Para mostrar imagenes en el administrador
from django.utils.html import format_html

# Register your models here.

# Personalizar el administrador django de Empleado
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'names', 
        'last_name', 
        'full_name',
        'job', 
        'department',
        'image_tag',
        'show_skill',
        )
    
    # Nueva funcion skills que no pertenece a la clase Empleado
    def show_skill(self, obj):
        return ", ".join([s.skill for s in obj.skills.all()])
        
    # def show_photo(self, obj):
    #     return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    
    # show_photo.short_description = 'Foto'
    show_skill.short_description = 'Habilidades'
    
    search_fields = (
        'names',
        'last_name',
        'job__job_name',
        'department__department_name',
        )
    
    list_filter = (
        'department',
        'job',
        'skills',
        )
    
    filter_horizontal = (
        'skills',
        )
    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidad)
