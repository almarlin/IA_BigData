def factorial(n):
    tot = 1
    for i in range(1, n + 1):
        tot = tot * i
        print(tot)
    return tot


num = int(input("Inserta un número para conocer su factorial: "))

print(f"Este es el factorial de {num}: {factorial(num)}")
