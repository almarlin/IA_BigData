FROM nginx:latest

# Copia el archivo de configuración de Nginx
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Copia los archivos de la aplicación web al contenedor
COPY ./www /var/www/html

# Exponer el puerto 80 para el servidor web
EXPOSE 80
