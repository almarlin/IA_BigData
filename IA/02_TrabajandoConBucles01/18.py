numeros = list([234, 135, 12, 0, 56, 7, 32, 35, 3])

print(f"Lista: {numeros}")

prom = 0
tot = 0
tam = len(numeros)
for numero in numeros:
    tot += numero

prom = tot/tam

print(f"El promedio es: {prom}")