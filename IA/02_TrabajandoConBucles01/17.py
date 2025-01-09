num = int(input("Introduce un número: "))
pot = int(input("Introduce su potencia: "))

tot = num

for i in range(1,pot):
    tot = tot * num

print(f"El cálculo es: {tot}")