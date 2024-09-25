from django.db import models
from applications.departamentos.models import Departamento
from PIL import Image
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField

import os
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# Create your models here.
# APP HABILIDADES
class Habilidad(models.Model):
    skill = models.CharField('Habilidad', max_length=60)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return self.skill


# APP EMPLEADOS
# Función para validar las extensiones de los archivos de imagen
def validar_extension_imagen(value):
    ext = os.path.splitext(value.name)[1]  # obtiene la extensión del archivo
    extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
    if ext.lower() not in extensiones_validas:
        raise ValidationError(f'Extensión no válida: {ext}. Solo se permiten archivos con las siguientes extensiones: {", ".join(extensiones_validas)}')

# Función que genera la ruta de guardado usando el ID del empleado
@deconstructible
class CustomImagePath:
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # Guardar la imagen usando el ID del empleado
        filename = f'{instance.id}.{ext}'
        return f'empleados_img/{filename}'
    

class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'Desarrollador'),
        ('1', 'Diseñador'),
        ('2', 'Tester'),
        ('3', 'Analista'),
        ('4', 'OTRO')
    )

    names = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombre Completo', 
        max_length=120, 
        editable=False,
        blank=True
        )
    job = models.CharField('Trabajo', max_length=60, choices=JOB_CHOICES)
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(
        'Foto', 
        upload_to=CustomImagePath(),
        validators=[validar_extension_imagen], 
        null=True, blank=True)
    skills = models.ManyToManyField(Habilidad)
    resume = RichTextField('Hoja de vida')


    def save(self, *args, **kwargs):
        if not self.id:  # Si la instancia no tiene ID aún, guardarla primero
            saved_image = self.image
            self.image = None  # Elimina la imagen temporalmente para evitar conflictos
            super().save(*args, **kwargs)
            self.image = saved_image  # Restaura la imagen luego de haber guardado el ID
        super().save(*args, **kwargs)  # Guardar nuevamente con la imagen
           
           
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "Sin imagen"

    image_tag.short_description = 'Imagen'


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['names', 'last_name']
        unique_together = ('names', 'department')


    def __str__(self):
        return f"{str(self.id)} {self.names} {self.last_name}"
        

'''
    def save(self, *args, **kwargs):
        # Guardar el empleado primero para obtener un ID si no lo tiene aún
        super().save(*args, **kwargs)
        
        # Verificar si hay una imagen cargada y si el empleado ya tiene un ID
        if self.image and not self.image.name.startswith(str(self.id)):
            # Definir un nuevo nombre para la imagen
            # new_filename = f"empleados/{self.id}.jpg"  # Cambia la extensión si la imagen no es JPG
            # Obtener la extensión original de la imagen
            extension = os.path.splitext(self.image.name)[1]
            new_filename = f"{self.id}{extension}"
            # Obtener la ruta anterior de la imagen
            old_path = self.image.path
            # Definir la nueva ruta para la imagen
            new_path = os.path.join(os.path.dirname(old_path), new_filename)
            # Renombrar el archivo
            os.rename(old_path, new_path)
            # Actualizar el campo de imagen con el nuevo nombre y volver a guardar
            self.image.name = f"empleados_img/{new_filename}"
            super().save(*args, **kwargs)
            # Redimensionar la imagen
            img = Image.open(new_path)
            img.thumbnail((300, 300))
            img.save(new_path)
            # Eliminar la imagen anterior
            # os.remove(old_path)
            # Actualizar el campo de imagen con el nuevo nombre y volver a guardar
            self.image.name = f"empleados_img/{new_filename}"
            super().save(*args, **kwargs)

            return super().save(*args, **kwargs)
'''