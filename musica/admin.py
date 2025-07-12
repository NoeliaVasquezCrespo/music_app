from django.contrib import admin

# Register your models here.
from .models import Artista, Album, Cancion, Playlist


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha_debut', 'descripcion')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('tipo',)

admin.site.register(Artista, ArtistaAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'fecha_lanzamiento', 'disponible')
    ordering = ('titulo',)
    search_fields = ('titulo', 'artista__nombre')
    list_filter = ('disponible',)

admin.site.register(Album, AlbumAdmin)

class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'genero', 'duracion_segundos')
    ordering = ('titulo',)
    search_fields = ('titulo', 'album__titulo')
    list_filter = ('genero',)

admin.site.register(Cancion, CancionAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'created_at')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    
admin.site.register(Playlist, PlaylistAdmin)
