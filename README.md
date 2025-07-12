# MUSICAPP

Elaborado por Noelia Vásquez Crespo

Pasos: 

## Instalar dependencias

- Se recomienda utilizar un entorno virtual (virtualenv)

```sh
pip install -r requirements.txt
```

## Cargar datos iniciales

```sh
python manage.py migrate
python manage.py loaddata dump_musica
```

## Ejecutar servidor de desarrollo

```sh
python manage.py runserver
```