import re

def crear_listin():
    with open("listin.txt","w",encoding="utf-8") as f:
        f.write("")
    return "Listin creado"

def anyadir_num(nombre,num):
    with open("listin.txt","r",encoding="utf-8") as f:
       data =  f.readlines()
    
    dataStr = ""
    for d in data:
        dataStr += f"{d}"

    dataStr += f"{nombre},{num}\n"
    with open("listin.txt","w",encoding="utf-8") as f:
        f.write(dataStr)
    return "Número añadido"

def get_num(nombre):
    with open("listin.txt","r",encoding="utf-8") as f:
        data = f.readlines()

    for l in data:
        cliente, telefono = l.strip().split(',')
        if cliente.lower() == nombre.lower():
            return f"El número de {nombre} es: {telefono}"
        
    return "Número no encontrado"

def eliminar_num(nombre):
    with open("listin.txt","r",encoding="utf-8") as f:
        data = f.readlines()

    for l in data:
        cliente, telefono = l.strip().split(',')
        if cliente.lower() == nombre.lower():
            data.remove(l)
    
    with open("listin.txt","w",encoding="utf-8") as f:
        f.writelines(data)
        
    return "Número eliminado"


crear_listin()  # Crea el archivo si no existe
anyadir_num("Juan Pérez", "123456789")  # Añade un cliente
anyadir_num("Ana Gómez", "987654321")  # Añade otro cliente

print(get_num("Juan Pérez"))  # Consulta el número de Juan
print(get_num("Luis Martínez"))  # Consulta un número que no existe

eliminar_num("Juan Pérez")  # Elimina a Juan del listín
print(get_num("Juan Pérez"))

