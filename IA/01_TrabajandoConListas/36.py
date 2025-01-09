frases = list(["Hola mundo","Buenas tardes","Winter is coming", "Dividir cadenas es fácil"])

palabras = [frase.split() for frase in frases]

# Mostrar el resultado
for palabra in palabras:
    print(palabra)