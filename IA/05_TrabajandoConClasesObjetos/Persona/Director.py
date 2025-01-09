from .Persona import Persona

class Director(Persona):
    def __init__(self, nombre, edad, genero, centro):
        super().__init__(nombre, edad, genero)
        self.centro = centro

    def informacion(self):
        return super().informacion() + f" es director del centro {self.centro}"
    
    def supervisar(self):
        return "Se ha comenzado la supervisión."
    

