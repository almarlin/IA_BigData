import hashlib

# Ejercicio: Verificación de Integridad de Archivos con Hashes
#
# Descripción:
# En esta práctica, implementarás un sistema de sumas de verificación utilizando distintos métodos de cifrado de la librería hashlib en Python.
# Deberás calcular, guardar y verificar hashes de archivos para comprobar su integridad.
#Requisitos:
# Crear un script en Python que realice las siguientes tareas:
# Calcular el hash SHA-256 de un archivo de texto (archivo.txt).
# Calcular el hash MD5 de una imagen (imagen.jpg).
#Calcular el hash SHA-1 de un archivo PDF (documento.pdf).
#Calcular el hash SHA-512 de un archivo ZIP (comprimido.zip)
# Calcular el hash SHA-1 de un archivo EXE (ejecutable.exe)
#Guardar los hashes calculados en un archivo de texto llamado hashes.txt, donde cada línea contenga el #nombre del archivo seguido de su respectivo hash.
#Implementar una función que permita verificar la integridad de un archivo comparando su hash actual #con un hash previamente calculado y almacenado en hashes.txt.
#Probar la función de verificación con los archivos proporcionados y mostrar un mensaje que indique si #el archivo ha sido modificado o no.﻿
#
# Instrucciones:
# 1. Selecciona cada archivo en tu pc.
# 2. Ingresa un algoritmo de hash (md5, sha1, sha256, sha512).
# 3. Genera y almacena el hash del archivo en un archivo de texto.
# 4. Verifica la integridad del archivo comparándolo con su hash.
# 5. Modifica el archivo original y vuelve a ejecutar la verificación para observar los resultados.
# 6. Documenta tu proceso con capturas de pantalla y explica los resultados obtenidos.

sha256 = hashlib.sha256()
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha512 = hashlib.sha512()

# Hay que leer el archivo en formato bytes para poder hashearlo
with open("el_quijote.txt","rb") as f:
    # Leemos por bloques de bytes (4096), lo indicamos con b""
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256.update(byte_block)

with open("rf_resultados.png","rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        md5.update(byte_block)

with open("blank.pdf","rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha1.update(byte_block)

with open("calidadDatos.rar","rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha512.update(byte_block)

with open("checksums.txt","w",encoding='utf-8') as f:
    f.write("el_quijote.txt: "+sha256.hexdigest()+"\n")
    f.write("rf_resultados.png: "+md5.hexdigest()+"\n")
    f.write("blank.pdf: "+sha1.hexdigest()+"\n")
    f.write("calidadDatos.rar: "+sha512.hexdigest()+"\n")

# Reiniciamos el objeto
sha1 = hashlib.sha1()

with open("python-3.10.0-amd64.exe","rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha1.update(byte_block)

with open("checksums.txt","a") as f:
    f.write("python-3.10.0-amd64.exe: "+sha1.hexdigest())


