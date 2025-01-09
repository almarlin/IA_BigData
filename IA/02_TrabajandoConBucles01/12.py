a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

mcm = max(a, b)

while not (mcm % a == 0 and mcm % b == 0):
    mcm += 1  


print(f"El MCM de {a} y {b} es {mcm}.")