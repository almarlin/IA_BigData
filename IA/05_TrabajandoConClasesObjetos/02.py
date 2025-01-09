class Persona:
    def __init__(self, nombre, edad, genero, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
    def saludar(self, persona):
        return f"{self.nombre} saluda a {persona.nombre}"
    def mayor_edad(self):
        if self.edad > 18:
            return "es mayor de edad"
        else:
            return "no es mayor de edad"
    def cinco_anyos(self):
        return f"{self.nombre} dentro de 5 años tendrá {self.edad+5}"
    
persona = Persona("Álvaro",22,"Hombre",1.68)
persona2 = Persona("Javi",22,"Hombre",1.76)

print(f"{persona.saludar(persona2)}")
print(f"{persona.nombre} {persona.mayor_edad()}")
print(f"{persona.cinco_anyos()}")