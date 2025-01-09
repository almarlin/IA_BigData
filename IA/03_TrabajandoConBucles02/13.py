num = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num < num2:
    print(f"{num2} es el número mayor")
elif num > num2:
    print(f"{num} es el número mayor")
else:
    print("Los numeros son iguales.")