nombres = list(["Paul", "Jessica", "Duncan", "Thufir", "Gurney", "Alia"])
grupo1 = list()
grupo2 = list()

for i, nombre in enumerate(nombres):
    if i % 2 == 0:
        grupo1.append(nombre)
    else:
        grupo2.append(nombre)

print("Grupo 1: ", grupo1)
print("Grupo 2: ", grupo2)
