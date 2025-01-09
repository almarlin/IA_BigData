from .Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, genero, asignatura):
        super().__init__(nombre, edad, genero)
        self.asignatura = asignatura

    def informacion(self):
        return super().informacion() + f" imparte {self.asignatura}"
    
    def enseñar(self):
        return f"Ha comenzado la clase de {self.asignatura}"