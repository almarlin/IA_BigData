import json
import re
from datetime import datetime


def cargar_datos(fichero):
    with open(fichero, "r") as f:
        return json.load(f)


def patron_email(email):
    # Comienza por letras (mayus o minus), numeros o algun caracter. Despues @ seguido de letras (mayus o minus) y numeros y finaliza con . + letras (mayus o minus) y numeros 
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, email))


def patron_telefono(telefono):
    # Una ocurrencia de 6, 7 o 9, y 8 ocurrencias de numeros entre 0 y 9
    patron = r'^[679]{1}[0-9]{8}$'
    return bool(re.match(patron, telefono))


def patron_codigo_postal(codigo_postal):
    # 5 numeros (\d devuelve solo numeros y {n} indica la cantidad de ocurrencias)
    patron = r'^\d{5}$'
    return bool(re.match(patron, codigo_postal))


def patron_matricula(matricula):
    # 4 ocurrencias de numeros y 3 de letras mayusculas
    patron = r'^\d{4}[A-Z]{3}$'
    return bool(re.match(patron, matricula))


def patron_ano(ano):
    anyo_actual = datetime.now().year
    return 1900 <= ano <= anyo_actual


def validar_alumno(alumno):
    if not patron_email(alumno['email']):
        print(f"Email inválido para {alumno['nombre']}")
    if not patron_telefono(alumno['telefono']):
        print(f"Teléfono inválido para {alumno['nombre']}")
    if not patron_codigo_postal(alumno['codigo_postal']):
        print(f"Código postal inválido para {alumno['nombre']}")
    return patron_email(alumno['email']) and patron_telefono(alumno['telefono']) and patron_codigo_postal(alumno['codigo_postal'])


def validar_vehiculo(vehiculo):
    if not patron_matricula(vehiculo['matricula']):
        print(f"Matrícula inválida para el vehículo {vehiculo['marca']} {vehiculo['modelo']}")
    if not patron_ano(vehiculo['anyo']):
        print(f"anyo inválido para el vehículo {vehiculo['marca']} {vehiculo['modelo']}")
    if not patron_email(vehiculo['propietario_email']):
        print(f"Email inválido para el propietario del vehículo {vehiculo['marca']} {vehiculo['modelo']}")
    return patron_matricula(vehiculo['matricula']) and patron_ano(vehiculo['anyo']) and patron_email(vehiculo['propietario_email'])



# Carga de datos
alumnos = cargar_datos("alumnos.json")
vehiculos = cargar_datos("vehiculos.json")

# Validar alumnos
for alumno in alumnos:
    if validar_alumno(alumno):
        print(f"Alumno {alumno['nombre']} validado correctamente.")
    else:
        print(f"Alumno {alumno['nombre']} tiene errores en los datos.")

# Validar vehiculos
for vehiculo in vehiculos:
    if validar_vehiculo(vehiculo):
        print(f"Vehículo {vehiculo['marca']} {vehiculo['modelo']} validado correctamente.")
    else:
        print(f"Vehículo {vehiculo['marca']} {vehiculo['modelo']} tiene errores en los datos.")
