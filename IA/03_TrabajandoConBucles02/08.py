num = int(input("Introduce un número para ver los impares: "))

for i in range(1,num):
    if i % 2 != 0:
        print(f"{i}")