from django.db import models

# Create your models here.
class PruebaBBDD(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo
    
