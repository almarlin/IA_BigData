import json

def filtrarCat(prod,categoria):

    filtrados = list()
    for p in prod:
        if p["categoria"].lower() == categoria.lower():
            filtrados.append(p)

    return filtrados

def totalInv(prod):
    tot = 0
    for p in prod:
        tot += p["precio"]

    return tot


def actStock(prod,stock,producto):

    for p in prod:
        if p["nombre"].lower() == producto.lower():
            p["stock"] = stock
    return prod

# Productos iniciales
productos = [
    {"nombre": "Manzanas", "categoria": "Frutas", "precio": 1.2, "stock": 100},
    {"nombre": "Plátanos", "categoria": "Frutas", "precio": 0.8, "stock": 150},
    {"nombre": "Leche", "categoria": "Lácteos", "precio": 1.5, "stock": 50},
    {"nombre": "Pan", "categoria": "Panadería", "precio": 1.0, "stock": 70},
    {"nombre": "Huevos", "categoria": "Huevos", "precio": 2.5, "stock": 30},
    {"nombre": "Arroz", "categoria": "Cereales", "precio": 1.0, "stock": 200},
    {"nombre": "Pasta", "categoria": "Cereales", "precio": 1.2, "stock": 120},
    {"nombre": "Tomates", "categoria": "Vegetales", "precio": 1.8, "stock": 80},
    {"nombre": "Cebollas", "categoria": "Vegetales", "precio": 1.0, "stock": 90},
    {"nombre": "Pollo", "categoria": "Carnes", "precio": 5.0, "stock": 40},
]

with open ("productos.json", "r") as f:
    fich = json.load(f)
    prod = fich.get("productos",[])

prod.extend(productos)

with open ("productosCopy.json","w") as f:
    json.dump({"productos":prod}, f , indent=4)


categorias = {p["categoria"] for p in prod}
print(f"Categorías: {categorias}")
categoria = input("¿Qué categoría quieres filtrar?\n")

nombres = {f["nombre"] for f in filtrarCat(prod, categoria)}

print(f"Los productos de esa categoría son: {nombres}")
print(f"El valor total del inventario es: {totalInv(prod)}")

stock = int(input(f"Introduce el nuevo stock de {prod[0]["nombre"]}\n"))

prod = actStock(prod,stock,prod[0]["nombre"])

with open ("productosCopy.json","w") as f:
    json.dump({"productos":prod},f,indent=4)