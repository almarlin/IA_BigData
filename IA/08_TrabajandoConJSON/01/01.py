import json
import random

# Listas de nombres y apellidos
nombres = [ "María", "Carlos", "Ana", "Luis", "Pedro", "Sofía", "Jorge", "Lucía"]
apellidos = ["García", "Martínez", "López", "Hernández", "González", "Pérez","Flores"]

with open ("contactos.json", "r") as f:
    fichero = json.load(f)
    contactos = fichero.get("contactos",[])



tamanyoOriginal = len(contactos)

while len(contactos) < tamanyoOriginal + 10:

    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)

    contactos.append({"nombre": nombre , "apellido": apellido, "telefono": random.randint(600000000, 699999999), "correo": nombre+apellido+'@example.com'})

with open ("contactosCopy.json", "w") as f:
    json.dump({"contactos":contactos}, f, indent=4)


with open ("contactosCopy.json", "r") as f:
    fichero = json.load(f)
    contactos = fichero.get("contactos",[])

nombre = input("¿Qué contacto desea buscar?\n")
datos = [contacto for contacto in contactos if contacto["nombre"].lower() == nombre.lower()]
print(f"Estos son los datos: {datos}")
tlf = int(input(f"Acualice el número de teléfono del contacto:\n"))

for contacto in contactos:
    if datos[0] == contacto:
        contacto["telefono"] = tlf
        break
print("Número actualizado correctamente.")

with open ("contactosCopy.json", "w") as f:
    json.dump({"contactos":contactos}, f, indent=4)

