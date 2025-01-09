import json

# Funciones
def cargarAlumnos(alumnos):

    with open("alumnos.json", "r") as f:
        fich = json.load(f)
        orig = fich["alumnos"]

    orig.extend(alumnos)

    with open("alumnosCopy.json", "w") as f:
        json.dump({"alumnos": orig}, f, indent=4)

    return orig

def addAlumnos(alumno):
    with open("alumnosCopy.json", "r") as f:
        fich = json.load(f)
        orig = fich["alumnos"]
    orig.append(alumno)
    with open("alumnosCopy.json", "w") as f:
        json.dump({"alumnos": orig}, f, indent=4)

    return orig

def rmAlumnos(al,orig):
    alumnos = [alumno for alumno in orig if alumno["nombre"].lower() != al["nombre"].lower()]
    orig = cargarAlumnos(alumnos)
    return orig


def filtAprob(orig):
    filtrados = list()

    for a in orig:
        if a["calificacion"] >=50:
            filtrados.append(a)

    return filtrados

def edadPromedio(orig):
    tot = 0

    for a in orig:
        tot += a["edad"]
    
    prom = tot / len(orig)

    return prom

# Valores
alumnos_iniciales = [
    {"nombre": "Juan", "edad": 19, "calificacion": 70, "ciudad": "Valencia"},
    {"nombre": "Ana", "edad": 21, "calificacion": 65, "ciudad": "Sevilla"},
    {"nombre": "Pedro", "edad": 23, "calificacion": 55, "ciudad": "Zaragoza"},
    {"nombre": "Sofía", "edad": 20, "calificacion": 95, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 22, "calificacion": 58, "ciudad": "Barcelona"},
    {"nombre": "María", "edad": 24, "calificacion": 80, "ciudad": "Valencia"},
    {"nombre": "Jorge", "edad": 21, "calificacion": 45, "ciudad": "Sevilla"}
]

# Flujo

orig = cargarAlumnos(alumnos_iniciales)
aprobados = filtAprob(orig)

print("Lista de apobados")
for a in aprobados:
    print(f"{a["nombre"]} | {a["calificacion"]}")

print(f"La edad promedio es: {edadPromedio(orig)}")

nombre= input("\nNombre del alumno\n")
edad= int(input("Edad del alumno\n"))
calificacion= int(input("Calificacion del alumno (sobre 100)\n"))
ciudad= input("Ciudad del alumno\n")

alumno = {
    "nombre":nombre,
    "edad": edad,
    "calificacion":calificacion,
    "ciudad":ciudad
}

orig = addAlumnos(alumno)
print(f"\nSe ha añadido a {alumno["nombre"]}")
for a in orig:
    print(f"{a["nombre"]}")

orig = rmAlumnos(alumno,orig)
print(f"\nSe ha eliminado a {alumno["nombre"]}")
for a in orig:
    print(f"{a["nombre"]}")