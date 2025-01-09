palabras = list(
    [
        "Botón",
        "Cajón",
        "Albornoz",
        "Ordenador",
        "Teclado",
        "Instrumento",
        "Armario",
        "Oro",
        "Tecnologia",
        "Alfajor",
    ]
)
cont = 0

letra = input("Introduce una letra: ")
letraUpr = letra.upper()

for palabra in palabras:
    if palabra[0] == letraUpr:
        cont+=1

print(f"Esta es la lista: {palabras}")
print(f"{cont} palabras empiezan por la letra {letra}")