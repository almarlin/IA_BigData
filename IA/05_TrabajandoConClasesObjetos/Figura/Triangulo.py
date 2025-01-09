from .Figura import Figura


class Triangulo(Figura):
    def __init__(self, color, tipo, base, altura, lado):
        super().__init__(color, tipo)
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcularArea(self):
        return (self.base * self.altura) / 2
    
    def calcularPerimetro(self):
        return self.lado * 2 + self.base
