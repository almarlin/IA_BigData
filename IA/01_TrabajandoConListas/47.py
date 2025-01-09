numeros = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 8, 9, 10, 5]

numeros_unicos = set()
duplicados = []

for numero in numeros:
    if numero in numeros_unicos:
        duplicados.append(numero) 
    else:
        numeros_unicos.add(numero) 


lista_sin_duplicados = list(numeros_unicos)

print("Duplicados encontrados:", duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)