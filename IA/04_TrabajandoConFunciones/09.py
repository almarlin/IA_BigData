def ordenar_lista(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        temp = lista[i]
        lista[i] = lista[min_index]
        lista[min_index] = temp

numeros = [64, 25, 12, 22, 11]
ordenar_lista(numeros)
print("Lista ordenada:", numeros)


