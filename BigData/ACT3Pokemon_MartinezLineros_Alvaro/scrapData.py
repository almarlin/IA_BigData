import requests
from bs4 import BeautifulSoup
import json


url = "https://nintendo.fandom.com/wiki/Category:Pokémon_trainers"

# Solicitud de la pagina
response = requests.get(url)

if response.status_code == 200:
    # Parsea el contenido
    soup = BeautifulSoup(response.text, "html.parser")

    # Encuentra la sección que contiene los entrenadores
    entrenadores = []

    # Asumiendo que los datos de los entrenadores están en tablas
    for a in soup.find_all("a", class_="category-page__member-link"):
        nombre = a.get_text(strip=True)
        entrenadores.append(
            {
                "nombre": nombre,
            }
        )

    # Mostrar los datos extraídos
    for entrenador in entrenadores:
        print(entrenador)

oldTrainers = entrenadores
url = "https://nintendo.fandom.com/wiki/Category:Pokémon_trainers?from=Miriam"
# Solicitud de la pagina
response = requests.get(url)

if response.status_code == 200:
    # Parsea el contenido
    soup = BeautifulSoup(response.text, "html.parser")

    # Encuentra la sección que contiene los entrenadores
    entrenadores = []

    # Asumiendo que los datos de los entrenadores están en tablas
    for a in soup.find_all("a", class_="category-page__member-link"):
        nombre = a.get_text(strip=True)
        entrenadores.append(
            {
                "nombre": nombre,
            }
        )

    # Mostrar los datos extraídos
    for entrenador in entrenadores:
        print(entrenador)

oldTrainers += entrenadores

with open("entrenadores.json", "w") as fichero:
    json.dump(oldTrainers, fichero, indent=4)


url = "https://pokemon.fandom.com/es/wiki/Gimnasio_Pokémon"

tipo_traducciones = {
    "normal": "normal",
    "fuego": "fire",
    "agua": "water",
    "eléctrico": "electric",
    "planta": "grass",
    "hielo": "ice",
    "lucha": "fighting",
    "veneno": "poison",
    "tierra": "ground",
    "volador": "flying",
    "psíquico": "psychic",
    "bicho": "bug",
    "roca": "rock",
    "fantasma": "ghost",
    "dragón": "dragon",
    "siniestro": "dark",
    "acero": "steel",
    "hada": "fairy"
}

# Solicitud de la pagina
response = requests.get(url)

if response.status_code == 200:
    # Parsea el contenido
    soup = BeautifulSoup(response.text, "html.parser")

    # Encuentra la sección que contiene los entrenadores
    gimnasios = []

    # Asumiendo que los datos de los entrenadores están en tablas
    gimnasios = []  # Lista para almacenar gimnasios
    gimnasios_set = set()  # Conjunto para rastrear combinaciones únicas

    for h3 in soup.find_all("h3"):
        ul = h3.find_next_sibling("ul")

        if ul:
            regionSpan = h3.find_next("span")
            region = regionSpan.get_text(strip=True)

            if region and len(region)<10:
                for li in ul.find_all("li"):
                    for a in li.find_all("a"):
                        typee = a.get_text(strip=True)
                        if typee.startswith(("tipo")):
                            siguiente = a.find_next("a")
                            leader = siguiente.get_text(strip=True)

                            # Crear una clave única para cada gimnasio
                            key = (region, typee, leader)

                            # Verificar si la clave ya está en el conjunto
                            if key not in gimnasios_set:
                                gimnasios_set.add(key)  # Agregar la clave al conjunto

                                tipo_traducido = tipo_traducciones.get(typee[5:].lower(), typee[5:])
                                
                                gimnasios.append(
                                    {"region": region, "type": tipo_traducido, "leader": leader}
                                )



with open("gimnasios.json", "w") as fichero:

    json.dump(gimnasios, fichero, indent=4)
