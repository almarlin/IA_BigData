import json
from datetime import datetime

# Funciones
def cargarEventos(eventos):

    with open("eventos.json", "r") as f:
        fich = json.load(f)
        orig = fich["eventos"]

    orig.extend(eventos)

    with open("eventosCopy.json", "w") as f:
        json.dump({"eventos": orig}, f, indent=4)

    return orig

def filtFecha(fecha, orig):

    fecha = datetime.strptime(fecha, "%Y-%m-%d")
    filtrados = [evento for evento in orig if datetime.strptime(evento["fecha"], "%Y-%m-%d") >= fecha]
    return filtrados

def filtUbicacion(ubicacion, orig):

    filtrados = [evento for evento in orig if evento["ubicacion"].lower() == ubicacion.lower()]
    return filtrados

def eliminarEventosPasados(orig):

    hoy = datetime.today()
    filtrados = [evento for evento in orig if datetime.strptime(evento["fecha"], "%Y-%m-%d") >= hoy]
    return filtrados

def agregarEvento(evento, eventos):

    eventos.append(evento)
    cargarEventos(eventos)
    return eventos

# Valores iniciales
eventos_iniciales = [
    {"titulo": "Conferencia Wordpress", "fecha": "2024-12-18", "ubicacion": "Madrid", "organizador": "Wordpress España"},
    {"titulo": "Conferencia", "fecha": "2025-12-01", "ubicacion": "Sevilla", "organizador": "TechFest"}
]




# Flujo
eventos = cargarEventos(eventos_iniciales)

fecha = input("Introduce la fecha a partir de la cual deseas filtrar los eventos (yyyy-mm-dd): ")
eventos_filtrados_fecha = filtFecha(fecha, eventos)

print(f"\nEventos a partir de {fecha}:")
for evento in eventos_filtrados_fecha:
    print(f"{evento['titulo']} - {evento['fecha']} - {evento['ubicacion']} - {evento['organizador']}")

ubicacion = input("\nIntroduce la ubicación para filtrar los eventos: ")
eventos_filtrados_ubicacion = filtUbicacion(ubicacion, eventos)

print(f"\nEventos en {ubicacion}:")
for evento in eventos_filtrados_ubicacion:
    print(f"{evento['titulo']} - {evento['fecha']} - {evento['organizador']}")


eventos_sin_pasados = eliminarEventosPasados(eventos)

print(f"\nEventos futuros:")
for evento in eventos_sin_pasados:
    print(f"{evento['titulo']} - {evento['fecha']} - {evento['ubicacion']} - {evento['organizador']}")


print("\nAñadiendo un nuevo evento...")

titulo = input("Introduce el título del evento: ")
fecha = input("Introduce la fecha del evento (yyyy-mm-dd): ")
ubicacion = input("Introduce la ubicación del evento: ")
organizador = input("Introduce el organizador del evento: ")

nuevo_evento = {
    "titulo": titulo,
    "fecha": fecha,
    "ubicacion": ubicacion,
    "organizador": organizador
}


eventos = agregarEvento(nuevo_evento, eventos)


print(f"\nCatálogo de eventos actualizado:")
for evento in eventos:
    print(f"{evento['titulo']} - {evento['fecha']} - {evento['ubicacion']} - {evento['organizador']}")
