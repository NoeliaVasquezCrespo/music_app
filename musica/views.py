from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from datetime import date

from .models import Artista, Cancion, Album, Playlist
from .serializers import ArtistaSerializer, CancionSerializer, AlbumSerializer, PlaylistSerializer
from .serializers import ReporteCancionesSerializer, ReporteAlbumesSerializer


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
    
# Consulta para mostrar artistas de tipo "Solista"    
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
    
# Consulta para mostrar solo cantidad de álbumes lanzados desde el 01/01/2023 hasta la fecha actual   
@api_view(['GET'])
def album_contar(request):
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

# Consulta para mostrar canciones de género "Pop" y su cantidad
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
    
# Consulta para mostrar álbumes lanzados desde el 01/01/2023 hasta la fecha actual y su cantidad
@api_view(['GET'])
def album_contar_con_datos(request):
    try:
        albumes = Album.objects.filter(fecha_lanzamiento__range=('2023-01-01', date.today())) 
        cantidad_album = albumes.count()
       
        return JsonResponse(
            ReporteAlbumesSerializer({
                "cantidad": cantidad_album,
                "albumes": albumes,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)          