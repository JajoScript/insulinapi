# InsulinAPI

## Instalación

```bash
  # * Antes de instalar las dependencias. Se recomienda iniciar un entorno virtual.
  # Para crear un entorno virtual.
  $py -m venv <nombre_entorno>

  # Para activar el entorno en Bash:
  $.\<nombre_entorno>\Scripts\activate

  # Instalación de dependencias.
  $py pip install -r requirementes.txt
```

Recordatorio, se debe colocar todos los archivos relacionados al modelo de la IA en ruta _"/api/models/"_. Como se muestra en el siguiente esquema:

```
  .
  ├── api
  │   ├── __init__.py
  │   ├── server.py
  │   └── models
  │       ├── __init__.py
  │       ├── predict.py
  │       ├── modelo.h5
  │       └── pesos.h5
```

## Ejecución

Para ejecutar la API.

```bash
  $py main.py

  # Alternativa con uvicorn:
  $uvicorn api.server:app --reload
```

## Adicional

Como instalar Tensorflow.

```bash
  $python3 -m pip install tensorflow[and-cuda]
```
