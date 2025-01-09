tempsCel = list([0, 18, 22, 25, 27, 31, 33, 35, 38, 40, 41])

tempsFht = list()

for temp in tempsCel:
    fahrenheit = (temp * 9/5) + 32
    tempsFht.append(fahrenheit)

print("Celsius: ",tempsCel)
print("Fahrenheit: ",tempsFht)