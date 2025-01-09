class Vehiculo:
    def __init__(self, marca, modelo, anyo):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo

    def acelerar(self):
        return "Acelera"
    
    def frenar(self):
        return "Frena"
    
    def tocarClaxon(self):
        return "Toca el claxon"