numeros = list([234,134,12,0,56,7,32,35,2])

print("Todos los números:", numeros)

def es_mayor(numero):
    return numero > 5

mayores_de_cinco = list(filter(es_mayor, numeros))

print("Los mayores de 5:",mayores_de_cinco)