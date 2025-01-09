numero = int(input("Introduce un número entero positivo: "))

suma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:  
        suma_divisores += i 


if suma_divisores == numero:
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
