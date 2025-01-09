from .Animal import Animal

class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacerSonido(self):
        return f"{self.nombre} pía"
    
    def volar(self):
        return f"{self.nombre} echa a volar"