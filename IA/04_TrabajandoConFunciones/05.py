def sum(nums):
    tot=0
    for n in nums:
        tot += n

    return tot

numeros = list([3423,36,12,323,447,341,9])

print(f"La suma del contenido de la lista es: {sum(numeros)}")