num = int(input("Introduce un número para conocer su tabla de multiplicar: "))

print(f"\nTabla del {num}")
for n2 in range(1,11):
    print(f"{num} * {n2} = {num*n2}")