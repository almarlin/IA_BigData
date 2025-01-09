num = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
num3 = int(input("Introduce un último número: "))


if num == num2 == num3:
    print("Todos los números son iguales.")
elif num >= num2 and num >= num3:
    print(f"El mayor de los tres números es: {num}")
elif num2 >= num and num2 >= num3:
    print(f"El mayor de los tres números es: {num2}")
else:
    print(f"El mayor de los tres números es: {num3}")
