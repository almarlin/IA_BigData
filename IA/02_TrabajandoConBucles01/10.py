palabra = input("Introduce una palabra para contar sus vocales: ")

palabraLwr = palabra.lower()
ini = 0
cont = 0

for i in range(ini, len(palabra)):
    if palabraLwr[i] in "aeiou":
        cont += 1

print(f"La palabra {palabra} tiene {cont} vocales.")
