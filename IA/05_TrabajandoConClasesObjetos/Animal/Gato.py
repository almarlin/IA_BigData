from .Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacerSonido(self):
        return f"{self.nombre} maúlla"
    
    def aranyar(self):
        return f"{self.nombre} araña"