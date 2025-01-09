class Estudiante:
    def __init__(self,nombre, curso, notas):
        self.nombre = nombre
        self.curso = curso
        self.notas = notas
        self.promedio = self.calcProm()

    def nuevaNota(self, nota):
        self.notas.append(nota)
        self.calcProm()
        return f"Nota añadida correctamente."
    
    def calcProm(self):
        tot=0
        for n in self.notas:
            tot += n
        self.promedio = tot/len(self.notas)
        return f"El promedio de {self.nombre} es {self.promedio}"
    
    def aprobar(self):
        self.calcProm()
        if self.promedio >=5:
            return f"El estudiante ha aprobado."
        else:
            return f"El estudiante ha suspendido."
        



estudiante1 = Estudiante("Juan Pérez", "Matemáticas", [7, 8, 6])

print(estudiante1.calcProm())

print(estudiante1.nuevaNota(9)) 
print(estudiante1.calcProm())  

print(estudiante1.aprobar())