inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))
num = int(input("Introduce un numero para saber sus múltiplos en el rango: "))

multiplos = list()

for i in range(inicio,fin):
    if i % num == 0:
        multiplos.append(i)

print(f"Los múltiplos encontrados son: {multiplos}")