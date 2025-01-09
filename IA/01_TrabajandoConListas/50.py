from functools import reduce

numeros = list([1, 2, 3, 4, 5])

total = reduce(lambda x, y: x * y, numeros)

print("Lista: ",numeros)
print("Total: ",total)