from django.core.exceptions import ValidationError
from datetime import date


# Validar duración de la canción
def validar_duracion(value):
    if value <= 30:
        raise ValidationError('La duración de la canción debe ser mayor a 30 segundos', params={"value": value})

# Validar cantidad de caracteres de la descripción    
def validar_cantidad_caracteres(value):
    if len(value) < 10:
        raise ValidationError('La descripción debe tener al menos 10 caracteres', params={"value": value})
    
# Validar fecha de lanzamiento del álbum (no puede ser fecha futura)
def validar_fecha_lanzamiento(value):
    if value > date.today():
        raise ValidationError('La fecha de lanzamiento no puede ser futura', params={"value": value})
    