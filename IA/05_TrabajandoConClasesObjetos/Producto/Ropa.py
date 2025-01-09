from .Producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla, descuento):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.descuento = descuento

    def costoTotal(self):
        return super().costoTotal() - (self.precio * (self.descuento/100) * self.cantidad)
    