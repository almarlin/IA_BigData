numeros = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

tamanyo = len(numeros) // 4

resultado = list()

inicio = 0

for i in range(tamanyo):
    fin = inicio + tamanyo
    resultado.append(numeros[inicio:fin])
    inicio = fin


print("Original: ", numeros)
print("Dividida: ", resultado)
