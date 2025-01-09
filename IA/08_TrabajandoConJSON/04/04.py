import json
from datetime import datetime

# Funciones
def cargarVentas(ventas):

    with open("ventas.json", "r") as f:
        fich = json.load(f)
        orig = fich["ventas"]

    orig.extend(ventas)

    with open("ventasCopy.json", "w") as f:
        json.dump({"ventas": orig}, f, indent=4)

    return orig


def addVentas(venta):
    with open("ventasCopy.json", "r") as f:
        fich = json.load(f)
        orig = fich["ventas"]
    orig.append(venta)
    with open("ventasCopy.json", "w") as f:
        json.dump({"ventas": orig}, f, indent=4)

    return orig


def filtFecha(fecha, orig):
    filtrados = list()

    date = datetime.strptime(fecha,"%Y-%m-%d")
    for v in orig:
        origDate = datetime.strptime(v["fecha"],"%Y-%m-%d")
        if date <= origDate:
            filtrados.append(v)

    return filtrados


def filtProd(prod, orig):
    filtrados = list()
    for v in orig:
        if prod.lower() == v["producto"].lower():
            filtrados.append(v)

    return filtrados


def totVentas(orig):
    tot = 0
    for v in orig:
        tot += v["precio"] * v["cantidad"]

    return tot


# Ejemplo de ventas iniciales
ventas_iniciales = [
    {"producto": "Laptop", "cantidad": 2, "precio": 1500, "fecha": "2024-10-28"},
    {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"},
    {"producto": "Mouse", "cantidad": 10, "precio": 25, "fecha": "2024-10-29"},
    {"producto": "Monitor", "cantidad": 3, "precio": 300, "fecha": "2024-10-30"},
    {"producto": "Auriculares", "cantidad": 4, "precio": 80, "fecha": "2024-10-25"},
    {"producto": "Cámara", "cantidad": 1, "precio": 500, "fecha": "2024-10-28"},
    {"producto": "Microfono", "cantidad": 2, "precio": 150, "fecha": "2024-10-26"},
    {"producto": "Impresora", "cantidad": 2, "precio": 120, "fecha": "2024-10-23"},
    {"producto": "Laptop", "cantidad": 1, "precio": 1000, "fecha": "2024-10-25"},
    {"producto": "Teclado", "cantidad": 3, "precio": 50, "fecha": "2024-10-30"},
]


orig = cargarVentas(ventas_iniciales)
tot = totVentas(orig)
print(f"Total de las ventas {tot}")


prod = input("¿Qué producto quieres filtrar de las ventas?\n")
filtProductos = filtProd(prod,orig)

for v in filtProductos:
    print(f"{v["producto"]} | {v["cantidad"]} | {v["precio"]} | {v["fecha"]}")

fecha = input("¿A partir de que fecha quieres filtrar?\n")
filtFechas = filtFecha(fecha,orig)

for v in filtFechas:
    print(f"{v["producto"]} | {v["cantidad"]} | {v["precio"]} | {v["fecha"]}")

print("--------------------------------------------\n")
print("Añadiendo producto...\n")
nombre = input("Introduce el nombre del producto\n")
cantidad = input("¿Cuántos se han vendido?\n")
precio = input("¿A qué precio?\n")
fecha = input("¿Qué día? (yyyy-mm-dd)\n")

venta = {
    "producto":nombre,
    "cantidad":cantidad,
    "precio":precio,
    "fecha":fecha
}

addVentas(venta)