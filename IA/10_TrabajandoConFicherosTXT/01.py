import unicodedata
import string

with open("el_quijote.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

# 1. Contabilizar las palabras que aparecen en el fichero
# Se divide por espacios
palabras = contenido.split()
cantPalabras = len(palabras)

print(f"\nEl Quijote tiene {cantPalabras} palabras.")

# 2. Indicar cuántas veces aparece la palabra “Capítulo” en el documento.
# Se debe ignorar el formato de escritura (mayúsculas, minúsculas o ambas)

capitulos = 0
cont = 0
for palabra in palabras:
    palabra_limpia = (
        unicodedata.normalize("NFC", palabra).strip(string.punctuation).lower()
    )
    if palabra_limpia == "capítulo":
        capitulos += 1

print(f"\nLa palabra 'capítulo' en El Quijote aparece {capitulos} veces.")

# 3. Crear un fichero .txt por capítulo indicado en el documento. (Capitulo_XX.txt)

cap = list()
capitulos = 0

for palabra in palabras:

    palabra_normalizada = unicodedata.normalize("NFC", palabra).strip(
        string.punctuation
    )

    if palabra_normalizada in ["CAPÍTULO", "Capítulo"]:
        if capitulos > 0:
            completo = " ".join(cap)
            with open(
                f"Capitulos/Capitulo_{capitulos}.txt", "w", encoding="utf-8"
            ) as file:
                file.write(completo)

        capitulos += 1
        cap = list()

    cap.append(palabra)


# 4. Contabilizar cuántas veces aparece la palabra Dulcinea, Quijote y Sancho.

dulcinea = 0
quijote = 0
sancho = 0

for palabra in palabras:

    palabra_normalizada = unicodedata.normalize("NFC", palabra).strip(
        string.punctuation
    )

    if palabra_normalizada in ["Dulcinea"]:
        dulcinea += 1
    elif palabra_normalizada in ["Quijote"]:
        quijote += 1
    elif palabra_normalizada in ["Sancho"]:
        sancho += 1

print(f"\nDulcinea aparece {dulcinea} veces")
print(f"Quijote aparece {quijote} veces")
print(f"Sancho aparece {sancho} veces")


# 5. Generar un listado con las 10 palabras que más veces aparecen en el documento.

registradas = {}

for palabra in palabras:

    palabra_normalizada = (
        unicodedata.normalize("NFC", palabra).strip(string.punctuation).lower()
    )

    if palabra_normalizada in registradas:
        registradas[palabra_normalizada] += 1
    else:
        registradas[palabra_normalizada] = 1

palabras_ordenadas = sorted(registradas.items(), key=lambda item: item[1], reverse=True)
top_10_palabras = palabras_ordenadas[:10]
print("Top 10 palabras más frecuentes:")
for palabra, frecuencia in top_10_palabras:
    print(f"{palabra}: {frecuencia}")
print("\n")

# 6. Generar un índice de las palabras que más veces aparece y la primera línea en la
# que aparece.


registradasLinea = {}


lineas = contenido.splitlines()

for numLinea, linea in enumerate(lineas, 1):

    palabras = linea.split()

    for palabra in palabras:

        palabra_normalizada = (
            unicodedata.normalize("NFC", palabra).strip(string.punctuation).lower()
        )

        if palabra_normalizada in registradasLinea:
            registradasLinea[palabra_normalizada]["frecuencia"] += 1
        else:

            registradasLinea[palabra_normalizada] = {
                "frecuencia": 1,
                "linNum": numLinea,
            }

palabras_ordenadas = sorted(
    registradasLinea.items(), key=lambda item: item[1]["frecuencia"], reverse=True
)
top_10_palabras = palabras_ordenadas[:10]
print("Top 10 palabras más frecuentes con líneas:")
for palabra, datos in top_10_palabras:
    print(
        f"{palabra}: aparece {datos["frecuencia"]}: primera aparición en línea {datos["linNum"]}"
    )
print("\n")

# 7. Calcular la longitud media de las palabras contenidas en el fichero.

cant = len(palabras)
tot = 0
for palabra in palabras:
    tot += len(palabra)

print(f"\nLa longitud media de las palabras es: {(tot/cant):.2f} caracteres")

# 8. Mostrar las 5 frases más largas del documento.
frase = ""
frases = list()
for c in contenido:
    frase += c
    if c == "." or c == "?" or c == "!":
        frases.append(frase)
        frase = ""


frases_ordenadas = sorted(frases, key=lambda item: len(item), reverse=True)
top_frases = frases_ordenadas[:5]
print(f"\nLas 5 frases más largas de El Quijote son: \n")
for frase in top_frases:
    print(f"{frase}\n")