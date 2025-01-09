import json

# Funciones
def cargarLibros(libros):
    with open("libros.json", "r") as f:
        fich = json.load(f)
        orig = fich["libros"]

    orig.extend(libros)

    with open("librosCopy.json", "w") as f:
        json.dump({"libros": orig}, f, indent=4)

    return orig

def filtGenero(genero, orig):
    filtrados = list()
    for libro in orig:
        if libro["genero"].lower() == genero.lower():
            filtrados.append(libro)

    return filtrados

def filtAutor(autor, orig):
    filtrados = list()
    for libro in orig:
        if libro["autor"].lower() == autor.lower():
            filtrados.append(libro)

    return filtrados

def librosRecientes(orig):
    filtrados = [libro for libro in orig if libro["anyo"] > 2000]
    return filtrados

def agregarLibro(libro, libros):
    libros.append(libro)
    cargarLibros(libros)
    return libros


# Valores iniciales
libros_iniciales = [
    {"titulo": "Cien anyos de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "anyo": 1967},
    {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "anyo": 1605},
    {"titulo": "1984", "autor": "George Orwell", "genero": "Distopía", "anyo": 1949},
    {"titulo": "La Casa de los Espíritus", "autor": "Isabel Allende", "genero": "Ficción", "anyo": 1982},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil", "anyo": 1943},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "genero": "Misterio", "anyo": 2001},
    {"titulo": "Los Pilares de la Tierra", "autor": "Ken Follett", "genero": "Histórico", "anyo": 1989},
    {"titulo": "Harry Potter y la Piedra Filosofal", "autor": "J.K. Rowling", "genero": "Fantasía", "anyo": 1997},
    {"titulo": "La Metamorfosis", "autor": "Franz Kafka", "genero": "Existencialismo", "anyo": 1915},
    {"titulo": "El Código Da Vinci", "autor": "Dan Brown", "genero": "Misterio", "anyo": 2003}
]


# Flujo

libros = cargarLibros(libros_iniciales)


genero = input("Introduce el género de libros que deseas filtrar: ")
libros_filtrados_genero = filtGenero(genero, libros)

print(f"\nLibros del género {genero}:")
for libro in libros_filtrados_genero:
    print(f"{libro['titulo']} - {libro['autor']} - {libro['anyo']}")

autor = input("\nIntroduce el autor de libros que deseas filtrar: ")
libros_filtrados_autor = filtAutor(autor, libros)

print(f"\nLibros de {autor}:")
for libro in libros_filtrados_autor:
    print(f"{libro['titulo']} - {libro['genero']} - {libro['anyo']}")

libros_recientes = librosRecientes(libros)

print(f"\nLibros recientes (después de 2000):")
for libro in libros_recientes:
    print(f"{libro['titulo']} - {libro['autor']} - {libro['anyo']}")

print("\nAñadiendo un nuevo libro...")

titulo = input("Introduce el título del libro: ")
autor = input("Introduce el autor del libro: ")
genero = input("Introduce el género del libro: ")
anyo = int(input("Introduce el año de publicación: "))

nuevo_libro = {
    "titulo": titulo,
    "autor": autor,
    "genero": genero,
    "anyo": anyo
}

libros = agregarLibro(nuevo_libro, libros)

print(f"\nCatálogo de libros actualizado:")
for libro in libros:
    print(f"{libro['titulo']} - {libro['autor']} - {libro['genero']} - {libro['anyo']}")
