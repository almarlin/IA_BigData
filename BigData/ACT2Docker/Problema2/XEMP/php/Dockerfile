# Utiliza la imagen oficial de PHP con FPM
FROM php:8.0-fpm

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    libzip-dev \
    zlib1g-dev \
    && docker-php-ext-install mysqli zip

# Limpieza
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
