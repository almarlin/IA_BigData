i = int(input("Introduce un número para conocer su factorial: "))
total = 1
while i > 0:
    total *= i
    i -= 1

print("Factorial: ", total)
