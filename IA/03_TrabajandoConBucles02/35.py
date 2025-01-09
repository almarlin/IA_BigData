perfectos= list()

for numero in range(1,1000):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:  
            suma_divisores += i 
    if suma_divisores == numero:
        perfectos.append(numero)

print(f"Los números perfectos entre 1 y 1000 son: {perfectos}")

