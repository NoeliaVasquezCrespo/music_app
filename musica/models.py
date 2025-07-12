import uuid

from django.db import models
from .validators import validar_duracion, validar_fecha_lanzamiento, validar_cantidad_caracteres

class TipoArtista(models.TextChoices):
    SOLISTA = 'Solista', 'Solista'
    GRUPO = 'Grupo', 'Grupo'


class Artista(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nacionalidad = models.CharField(max_length=50)
    tipo = models.CharField(
        max_length=10,
        choices=TipoArtista.choices,
        default=TipoArtista.SOLISTA
    )
    fecha_debut = models.DateField()
    descripcion = models.TextField()


    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField(validators=[validar_fecha_lanzamiento])
    descripcion = models.TextField(validators=[validar_cantidad_caracteres])
    disponible = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50)
    creditos = models.TextField(validators=[validar_cantidad_caracteres])
    duracion_segundos = models.PositiveIntegerField(validators=[validar_duracion])

    def __str__(self):
        return self.titulo
    

class Playlist(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(validators=[validar_cantidad_caracteres])
    canciones = models.ManyToManyField(Cancion)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre    
