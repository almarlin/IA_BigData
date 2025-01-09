def sumDig(num):
    numStr = str(num)
    tot = 0
    for n in numStr:
        tot += int(n)
    return tot

n = int(input("Introduce un número: "))

print(f"La suma de sus dígitos es: {sumDig(n)}")