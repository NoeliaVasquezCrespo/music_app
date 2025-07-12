from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from datetime import date

from .models import Artista, Cancion, Album, Playlist
from .serializers import ArtistaSerializer, CancionSerializer, AlbumSerializer, PlaylistSerializer
from .serializers import ReporteCancionesSerializer


# ModelViewSet para Artista y Cancion
class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer    

# GenericAPIView para Album y Playlist
class AlbumCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer   

class PlaylistCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer       
    
    
@api_view(['GET'])
def artista_solista(request):
    try:
        artistas = Artista.objects.filter(tipo='Solista')
        return JsonResponse(
            ArtistaSerializer(artistas, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    
@api_view(['GET'])
def album_count(request):
    try:
        cantidad_album = Album.objects.filter(fecha_lanzamiento__range=('2023-01-01', date.today())).count()
        return JsonResponse({
                'cantidad': cantidad_album
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)        

@api_view(['GET'])
def reporte_canciones(request):
    try:
        canciones = Cancion.objects.filter(genero='Pop')
        cantidad = canciones.count()
        return JsonResponse(
            ReporteCancionesSerializer({
                "cantidad": cantidad,
                "canciones": canciones,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)