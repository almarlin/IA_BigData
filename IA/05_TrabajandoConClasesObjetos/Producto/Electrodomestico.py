from .Producto import Producto

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, cantidad, consumo):
        super().__init__(nombre, precio, cantidad)
        self.consumo = consumo

    def costoTotal(self):
        return super().costoTotal()