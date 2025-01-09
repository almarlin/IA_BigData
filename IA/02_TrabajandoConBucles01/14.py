numeros = list([234, 135, 12, 0, 56, 7, 32, 35, 3])

print(f"Lista: {numeros}")

prev = 0
for numero in numeros:
    if numero > prev:
        prev = numero

print(f"El numero más grande es: {prev}")