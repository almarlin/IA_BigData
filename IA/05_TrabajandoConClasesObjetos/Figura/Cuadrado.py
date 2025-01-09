from .Figura import Figura

class Cuadrado(Figura):
    def __init__(self, color, tipo, lado):
        super().__init__(color, tipo)
        self.lado = lado
    
    def calcularArea(self):
        return self.lado * 2
    
    def calcularPerimetro(self):
        return self.lado * 4