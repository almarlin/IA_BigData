# Contiene una lista de tareas con detalles como descripción, fecha de vencimiento y
# estado. Insertar al menos 10 tareas al fichero.
# Agregar nuevas tareas, actualizar el estado de una tarea, filtrar tareas completadas.
import json
from datetime import datetime


# Funciones
def cargarTareas(tareas):

    with open("tareas.json", "r") as f:
        fich = json.load(f)
        orig = fich["tareas"]

    orig.extend(tareas)

    with open("tareasCopy.json", "w") as f:
        json.dump({"tareas": orig}, f, indent=4)


def addTarea(tarea):
    with open("tareasCopy.json", "r") as f:
        fich = json.load(f)
        orig = fich["tareas"]
    orig.append(tarea)
    with open("tareasCopy.json", "w") as f:
        json.dump({"tareas": orig}, f, indent=4)

def modTarea(tarea,estado):
    with open("tareasCopy.json", "r") as f:
        fich = json.load(f)
        orig = fich["tareas"]

    for t in orig:
        if t["descripcion"].lower() == tarea.lower():
            t["estado"] = estado

    with open("tareasCopy.json", "w") as f:
        json.dump({"tareas": orig}, f, indent=4)

def completadas():
    with open("tareasCopy.json", "r") as f:
        fich = json.load(f)
        orig = fich["tareas"]

    compl = list()

    for t in orig:
        if t["estado"] == "completada":
            compl.append(t)

    return compl



# Tareas iniciales
tareas_iniciales = [
    {
        "descripcion": "Estudiar Python",
        "vencimiento": "2024-11-01",
        "estado": "pendiente",
    },
    {
        "descripcion": "Revisar proyecto",
        "vencimiento": "2024-10-29",
        "estado": "completada",
    },
    {
        "descripcion": "Enviar informe",
        "vencimiento": "2024-10-30",
        "estado": "pendiente",
    },
    {
        "descripcion": "Preparar presentación",
        "vencimiento": "2024-11-05",
        "estado": "pendiente",
    },
    {
        "descripcion": "Llamar al cliente",
        "vencimiento": "2024-11-10",
        "estado": "pendiente",
    },
    {
        "descripcion": "Revisar correo electrónico",
        "vencimiento": "2024-10-28",
        "estado": "completada",
    },
    {
        "descripcion": "Comprar materiales",
        "vencimiento": "2024-11-03",
        "estado": "pendiente",
    },
    {
        "descripcion": "Organizar reunión",
        "vencimiento": "2024-11-01",
        "estado": "completada",
    },
    {
        "descripcion": "Enviar reporte financiero",
        "vencimiento": "2024-11-07",
        "estado": "pendiente",
    },
    {
        "descripcion": "Revisar tareas de la semana",
        "vencimiento": "2024-11-02",
        "estado": "completada",
    },
]


# Flujo principal

cargarTareas(tareas_iniciales)

print("Añadiendo una tarea nueva:")

descripcion = input("Introduce una descripción\n")
vencimiento = input("Introduce una fecha de vencimiento (YYYY-mm-dd) \n")
estado = input("Introduce el estado de la tarea\n")

tarea = {
        "descripcion": descripcion,
        "vencimiento": vencimiento,
        "estado": estado,
    }

addTarea(tarea)

modificar = input("¿Qué tarea quieres modificar?\n")
estado = input("¿Qué nuevo estado tiene esta tarea?\n")

modTarea(modificar,estado)

print(f"Las tareas completadas son:")

for t in completadas():
    print(f"{t["descripcion"]} | {t["vencimiento"]}")