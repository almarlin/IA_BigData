from .Vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anyo):
        super().__init__(marca, modelo,anyo)

    def acelerar(self):
        return super().acelerar()
    
    def frenar(self):
        return super().frenar()
    
    def tocarClaxon(self):
        return super().tocarClaxon()
    
    def bajarVentanillas(self):
        return "Se bajan las ventanillas"