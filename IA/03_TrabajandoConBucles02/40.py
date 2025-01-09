numero_decimal = int(input("Ingresa un número decimal: "))

binario = []

while numero_decimal > 0:
    residuo = numero_decimal % 2
    binario.append(str(residuo))
    numero_decimal = numero_decimal // 2

binario.reverse()

print("El número en binario es:", ''.join(binario))
