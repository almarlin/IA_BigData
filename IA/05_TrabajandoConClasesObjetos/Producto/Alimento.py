from .Producto import Producto
from datetime import datetime

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fechaCad):
        super().__init__(nombre, precio, cantidad)
        if isinstance(fechaCad, str):
            self.fechaCad = datetime.strptime(fechaCad, "%Y-%m-%d")
        else:
            self.fechaCad = fechaCad

    def costoTotal(self):
        if self.fechaCad.date() > datetime.today().date():

            return super().costoTotal()
        else:
            return "Producto caducado, retirar de existencias."

