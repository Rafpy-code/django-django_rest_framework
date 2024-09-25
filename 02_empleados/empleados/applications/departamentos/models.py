from django.db import models

# Create your models here.
class Departamento(models.Model):
    # ,null=True, blank=True, editable=False #Para que no se pueda editar el campo desde el admin de django
    # id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=50, unique=True)
    short_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']
        unique_together = ('name', 'short_name')
        
    def __str__(self):
        return self.name