import json

# Funciones
def cargarCoches(coches):

    with open("coches.json", "r") as f:
        fich = json.load(f)
        orig = fich["coches"]

    orig.extend(coches)

    with open("cochesCopy.json", "w") as f:
        json.dump({"coches": orig}, f, indent=4)

    return orig

def filtMarca(marca,orig):
    filtrados = list()
    for c in orig:
        if c["marca"].lower() == marca.lower():
            filtrados.append(c)

    return filtrados

def valorPromedio(orig):
    tot = 0

    for a in orig:
        tot += a["precio"]
    
    prom = tot / len(orig)

    return prom

def actualizarPrecio(marca, modelo, nuevo_precio, coches):
    for coche in coches:
        if coche["marca"].lower() == marca.lower() and coche["modelo"].lower() == modelo.lower():
            coche["precio"] = nuevo_precio
            break

    coches = cargarCoches(coches)
    return coches

# Valores iniciales
coches = [
    {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
    {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022},
    {"marca": "Honda", "modelo": "Civic", "precio": 22000, "año": 2024},
    {"marca": "Chevrolet", "modelo": "Malibu", "precio": 24000, "año": 2021},
    {"marca": "BMW", "modelo": "Serie 3", "precio": 35000, "año": 2020},
    {"marca": "Audi", "modelo": "A4", "precio": 33000, "año": 2021},
    {"marca": "Mercedes", "modelo": "Clase A", "precio": 37000, "año": 2022},
    {"marca": "Toyota", "modelo": "Yaris", "precio": 17000, "año": 2023},
    {"marca": "Ford", "modelo": "Mustang", "precio": 45000, "año": 2021},
    {"marca": "Hyundai", "modelo": "Elantra", "precio": 19000, "año": 2022}
    ]

# Flujo

# Flujo

coches_actualizados = cargarCoches(coches)
print(f"Coches después de cargar:\n{coches_actualizados}")

marca = input("Introduce la marca de coches que deseas filtrar: ")
coches_filtrados = filtMarca(marca, coches_actualizados)
print(f"\nCoches de la marca {marca}:")
for coche in coches_filtrados:
    print(f"{coche['marca']} {coche['modelo']} - {coche['precio']}€")

promedio = valorPromedio(coches_actualizados)
print(f"\nEl precio promedio de los coches es: {promedio}€")

marca_a_actualizar = input("\nIntroduce la marca del coche a actualizar: ")
modelo_a_actualizar = input("Introduce el modelo del coche a actualizar: ")
nuevo_precio = float(input("Introduce el nuevo precio: "))
coches_actualizados = actualizarPrecio(marca_a_actualizar, modelo_a_actualizar, nuevo_precio, coches_actualizados)

print(f"\nCoches después de actualizar el precio:")
for coche in coches_actualizados:
    print(f"{coche['marca']} {coche['modelo']} - {coche['precio']}€")