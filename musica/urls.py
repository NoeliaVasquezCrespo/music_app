from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'artistas', views.ArtistaViewSet)
router.register(r'canciones', views.CancionViewSet)

urlpatterns = [

    path('album/', views.AlbumCreateView.as_view(), name='album-create-list'),
    path('playlist/', views.PlaylistCreateView.as_view(), name='playlist-create-list'),
    

    path('artistas/tipo/solista', views.artista_solista, name='artista_solista'), 
    path('album/cantidad/', views.album_contar, name='album-contar'), 
    path('reporte/canciones/pop', views.reporte_canciones, name='reporte-canciones'),
    path('reporte/albumes/cantidad/', views.album_contar_con_datos, name='album-contar-con-datos'), 
    path('', include(router.urls)),

]