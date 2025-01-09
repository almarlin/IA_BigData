es_palindromo = lambda cadena: cadena == cadena[::-1]

texto = input("Introduce una cadena: ")

if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
