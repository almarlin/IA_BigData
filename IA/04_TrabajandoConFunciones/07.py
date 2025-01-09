def mcd(a, b):
    while b != 0:
        a, b = b, a % b  # Reemplaza a con b, y b con el residuo de a entre b
    return a

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

resultado = mcd(num1, num2)
print("El MCD de", num1, "y", num2, "es:", resultado)
