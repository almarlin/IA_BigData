num = 33

find= False
while find == False:
    intento = int(input("Introduce un numero entero entre 1 y 100: "))

    if num == intento:
        find = True
        print(f"¡Número secreto encontrado! {num}")
        break

    print("Número incorrecto, inténtalo de nuevo.")