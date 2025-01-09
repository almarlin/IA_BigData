nums = list([123,54,457,-123,-1245,-4,45,645])
tot = 0

for n in nums:
    if n > 0:
        tot += n

print(f"La lista de números: {nums}")
print(f"El total de la suma de los numeros positivos es: {tot}.")