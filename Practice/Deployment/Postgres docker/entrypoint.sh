#!/bin/bash

# Iniciar servicio de MySQL
service mysql start

# Esperar a que MySQL esté listo (ajusta el tiempo según tu necesidad)
sleep 10

# Configurar MySQL. Reemplaza 'yourpassword' con tu contraseña deseada
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';FLUSH PRIVILEGES;"

# Crear tu base de datos y cargar el esquema
mysql -u root -pyourpassword < /app/schema.sql

# Correr tu aplicación Flask
python3 /app/app.py
