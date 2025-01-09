mayor = lambda a,b: a>b

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if mayor(num1,num2):
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num2} es mayor que {num1}")