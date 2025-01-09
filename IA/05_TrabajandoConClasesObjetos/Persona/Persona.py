class Persona:
    def __init__(self,nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def informacion(self):
        return f"{self.genero}, {self.nombre}, {self.edad} años"