import json


# Funciones
def cargarSuperheroes(superheroes):
    with open("superheroes.json", "r") as f:
        fich = json.load(f)
        orig = fich["superheroes"]

    orig.extend(superheroes)

    with open("superheroesCopy.json", "w") as f:
        json.dump({"superheroes": orig}, f, indent=4)

    return orig


def filtCiudad(ciudad, orig):
    filtrados = [s for s in orig if s["ciudad"].lower() == ciudad.lower()]
    return filtrados


def filtEquipo(equipo, orig):
    filtrados = [s for s in orig if s["equipo"].lower() == equipo.lower()]
    return filtrados


def habilidadesUnicas(orig):
    habilidades = set()
    for s in orig:
        habilidades.update(s["habilidades"])
    return list(habilidades)


def agregarSuperheroe(superheroe, orig):
    orig.append(superheroe)
    with open("superheroesCopy.json", "w") as f:
        json.dump({"superheroes": orig}, f, indent=4)
    return orig


superheroes_iniciales = [
    {
        "alias": "El Fénix",
        "habilidades": ["renacimiento", "vuelo", "control de fuego"],
        "ciudad": "Valencia",
        "equipo": "Los Vengadores",
    },
    {
        "alias": "La Sombra",
        "habilidades": ["invisibilidad", "control de sombras"],
        "ciudad": "Madrid",
        "equipo": "Los Defensores",
    },
    {
        "alias": "El Titan",
        "habilidades": ["superfuerza", "invulnerabilidad"],
        "ciudad": "Barcelona",
        "equipo": "Los Vengadores",
    },
    {
        "alias": "Viento Celeste",
        "habilidades": ["control del viento", "manipulación del clima"],
        "ciudad": "Sevilla",
        "equipo": "Los Vengadores",
    },
    {
        "alias": "Centella",
        "habilidades": ["electromagnetismo", "velocidad"],
        "ciudad": "Granada",
        "equipo": "Los Defensores",
    },
]

superheroe_1 = {
    "alias": "El Halcón Rojo",
    "habilidades": ["vuelo", "visión nocturna"],
    "ciudad": "Sevilla",
    "equipo": "Los Vengadores",
}

superheroe_2 = {
    "alias": "El Rayo",
    "habilidades": ["velocidad", "manipulación de energía"],
    "ciudad": "Madrid",
    "equipo": "Los Defensores",
}

superheroes = cargarSuperheroes(superheroes_iniciales)
superheroes = agregarSuperheroe(superheroe_1, superheroes)
superheroes = agregarSuperheroe(superheroe_2, superheroes)

print("Habilidades únicas:", habilidadesUnicas(superheroes))

ciudad = input("Introduce la ciudad para filtrar superhéroes: ")
print(f"Superhéroes en {ciudad}: ", filtCiudad(ciudad, superheroes))

equipo = input("Introduce el equipo para filtrar superhéroes: ")
print(f"Superhéroes en el equipo {equipo}: ", filtEquipo(equipo, superheroes))
