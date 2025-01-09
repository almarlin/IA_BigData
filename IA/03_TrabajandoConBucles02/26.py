fin = int(input("¿Hasta que número quieres conocer los primos? "))

primos = list()

for num in range(1,fin):
    es_primo = True
    if num < 2:
        es_primo = False
    else:
        for i in range(2, num - 1):
            if num % i == 0:
                es_primo = False 
    if es_primo:
        primos.append(num)

print(f"Los numeros primos entre 0 y {fin} son: {primos}")