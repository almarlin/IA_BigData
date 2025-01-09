cadena = input("Introduce la cadena a cifrar: ")

cadena_cifrada = ""

for letra in cadena:
    if letra.isalpha():  
        if letra == 'z':
            nueva_letra = 'a'  
        elif letra == 'Z':
            nueva_letra = 'A'  
        else:
            nueva_letra = chr(ord(letra) + 1) 
    else:
        nueva_letra = letra  

    cadena_cifrada += nueva_letra

print(f"La cadena cifrada es: {cadena_cifrada}")
