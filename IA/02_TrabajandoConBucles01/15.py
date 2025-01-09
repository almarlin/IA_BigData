inicio = int(input("Introduce el número inicial del rango: "))
fin = int(input("Introduce el número final del rango: "))

suma_total = 0

for numero in range(inicio, fin + 1):
    suma_total += numero

print(f"La suma de todos los números de {inicio} a {fin} es {suma_total}.")