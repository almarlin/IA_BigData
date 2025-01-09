precios = list(
    [37.99, 29.99, 5.99, 259.99, 259.99, 2.59, 8.49, 7.34, 6.99, 8.99, 324.99]
)

promedio = 0
total = 0
for precio in precios:
    total += precio

promedio = total / len(precios)
promedio = round(promedio,2)

print("Precios: ", precios)
print("Promedio: ", promedio)
