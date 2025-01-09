inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el final del rango: "))

total = 0

for n in range(inicio, fin):
    if n % 2 == 0:
        total += n

print(f"El total de los numeros pares dentro del rango es: {total}")
