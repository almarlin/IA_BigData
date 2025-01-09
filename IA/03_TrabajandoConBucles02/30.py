num = int(input("Inserta un número: "))

tot = 0

while num >= 1:
    print(num)
    dig = num % 10
    tot += dig
    num = num // 10

print(f"El total de la suma de los dígitos es: {tot}")
