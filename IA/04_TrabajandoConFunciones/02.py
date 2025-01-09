def primo(num):
    es_primo = True
    if num < 2:
        es_primo = False
    else:
        for i in range(2, num - 1):
            if num % i == 0:
                    es_primo = False 
    return es_primo
        
n = int(input("Inserta un número: "))

if primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")