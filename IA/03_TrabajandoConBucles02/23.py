i = 0
nums = list()
pos = 0
neg = 0
cero = 0

while i < 3:
    nums.append(int(input("Introduce un número: ")))
    i += 1

for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        cero += 1

print(f"El resultado es: {pos} positivos, {neg} negativos y {cero} ceros")