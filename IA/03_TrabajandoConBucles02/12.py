num = int(input("Introduce un numero: "))

if num < 0:
    print(f"El numero {num} es negativo.")
elif num > 0:
    print(f"El numero {num} es positivo.")
else:
    print(f"El numero es 0.")
