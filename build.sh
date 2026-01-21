#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

# 1. Instalar las dependencias (usando el archivo que creamos antes)
pip install -r requirements.txt

# 2. Recolectar archivos estáticos (CSS, JS, Imágenes)
# Esto los pone en la carpeta 'staticfiles' para que WhiteNoise los sirva
python manage.py collectstatic --no-input

# 3. Aplicar migraciones a la base de datos de Render
# Esto asegura que tus tablas de Datos Personales existan en la nube
python manage.py migrate