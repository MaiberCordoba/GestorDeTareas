from django.db import models

# Create your models here.

class Tarea(models.model):
    estados = [{'terminado':'tarea finalizada'},
              {'icompleto':'tareas incompleta'}]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estado = models.CharField(choices=estados, default='icompleto')
    def __str__(self):
        return self.titulo
