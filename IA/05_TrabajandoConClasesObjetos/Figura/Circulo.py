from .Figura import Figura
import math

class Circulo(Figura):
    def __init__(self, color, tipo, radio):
        super().__init__(color, tipo)
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio **2)
    
    def calcularPerimetro(self):
        return 2 * self.radio * math.pi