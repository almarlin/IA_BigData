from .Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        super().__init__(nombre, edad, genero)
        self.curso = curso

    def informacion(self):
        return super().informacion() + f" {self.curso} curso"
    
    def estudiar(self):
        return f"{self.nombre} está estudiando."
    
