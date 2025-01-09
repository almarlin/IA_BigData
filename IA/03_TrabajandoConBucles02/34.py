numeros = list([234, 135, 12, 5, 56, 7, 32, 35, 3])

prev=numeros[0]
cond = True

for n in numeros:
    if n > prev:
        print(f"La lista no esta ordenada {n} > {prev}")
        cond = False
        break

    prev = n

if cond:
    print(f"La lista {numeros} está ordenada.")