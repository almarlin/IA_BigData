def contVoc(cad):
    cont = 0
    for c in cad:
        c = c.lower()
        if c in 'aeiou':
            cont += 1
    return cont

cadena = input("Introduce una cadena: ")

print(f"En la cadena '{cadena}' hay {contVoc(cadena)} vocales")
