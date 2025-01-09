import json


# Funciones
def cargarPeliculas(peliculas):

    with open("peliculas.json", "r") as f:
        fich = json.load(f)
        orig = fich["peliculas"]

    orig.extend(peliculas)

    with open("peliculasCopy.json", "w") as f:
        json.dump({"peliculas": orig}, f, indent=4)

    return orig


def filtGenero(genero, orig):

    filtrados = [
        pelicula for pelicula in orig if pelicula["genero"].lower() == genero.lower()
    ]
    return filtrados


def listarDirectores(orig):

    directores = {pelicula["director"] for pelicula in orig}
    return list(directores)


def agregarPelicula(pelicula, peliculas):

    peliculas.append(pelicula)
    cargarPeliculas(peliculas)
    return peliculas


# Valores iniciales
peliculas_iniciales = [
    {
        "titulo": "El Gran Hotel Budapest",
        "director": "Wes Anderson",
        "anyo": 2014,
        "genero": "Drama",
    },
    {
        "titulo": "La La Land",
        "director": "Damien Chazelle",
        "anyo": 2016,
        "genero": "Romance",
    },
]


peliculas = cargarPeliculas(peliculas_iniciales)

# Flujo

genero = input("Introduce el género por el cual deseas filtrar las películas: ")
peliculas_filtradas = filtGenero(genero, peliculas)

print(f"\nPelículas de género {genero}:")
for pelicula in peliculas_filtradas:
    print(f"{pelicula['titulo']} - {pelicula['director']} - {pelicula['anyo']}")


directores = listarDirectores(peliculas)

print("\nDirectores únicos:")
for director in directores:
    print(director)


print("\nAñadiendo una nueva película...")

titulo = input("Introduce el título de la película: ")
director = input("Introduce el director de la película: ")
anyo = input("Introduce el año de lanzamiento de la película: ")
genero = input("Introduce el género de la película: ")

nueva_pelicula = {
    "titulo": titulo,
    "director": director,
    "anyo": anyo,
    "genero": genero,
}


peliculas = agregarPelicula(nueva_pelicula, peliculas)


print(f"\nCatálogo de películas actualizado:")
for pelicula in peliculas:
    print(
        f"{pelicula['titulo']} - {pelicula['director']} - {pelicula['anyo']} - {pelicula['genero']}"
    )
