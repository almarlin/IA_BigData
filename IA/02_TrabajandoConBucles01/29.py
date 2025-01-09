cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

i = 0
longitud1 = len(cadena1)
longitud2 = len(cadena2)

while i < longitud1 and i < longitud2:
    if cadena1[i] == cadena2[i]:
        print(f"Caracter en la posición {i}: '{cadena1[i]}' es igual en ambas cadenas.")
    else:
        print(f"Caracter en la posición {i}: '{cadena1[i]}' en cadena1 y '{cadena2[i]}' en cadena2 son diferentes.")
    i += 1

if longitud1 > longitud2:
    print(f"\nLa primera cadena tiene caracteres adicionales: '{cadena1[i:]}'")
elif longitud2 > longitud1:
    print(f"\nLa segunda cadena tiene caracteres adicionales: '{cadena2[i:]}'")
