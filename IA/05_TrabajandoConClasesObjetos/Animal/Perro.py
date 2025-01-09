from .Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    def hacerSonido(self):
        return f"{self.nombre} ladra"
    
    def correr(self):
        return f"{self.nombre} echa a correr"