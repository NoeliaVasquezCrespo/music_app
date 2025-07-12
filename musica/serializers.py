from itertools import product

from rest_framework import serializers

from .models import Artista, Cancion, Album, Playlist


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class ReporteCancionesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    canciones = CancionSerializer(many=True)