cola = list()

persona1 = "Alvaro"
persona2 = "Federico"
persona3 = "Menganito"

print("La cola esta vacía: ",cola)

cola.append(persona1)
cola.append(persona2)
cola.append(persona3)

print("Ha llegado gente a la cola")
print("Estado de la cola: ",cola)

cola.pop(0)
cola.pop(0)

print("Se ha ido gente de la cola")
print("Estado de la cola: ",cola)