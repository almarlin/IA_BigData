# main.py
from Vehiculo.Coche import Coche
from Vehiculo.Motocicleta import Motocicleta
from Producto.Ropa import Ropa
from Producto.Alimento import Alimento
from Persona.Profesor import Profesor
from Persona.Estudiante import Estudiante
from Persona.Director import Director
from Figura.Triangulo import Triangulo
from Figura.Cuadrado import Cuadrado
from Figura.Circulo import Circulo
from Animal.Perro import Perro
from Animal.Gato import Gato
from Animal.Pajaro import Pajaro



coche = Coche("Toyota", "Corolla", 2020)
print(coche.acelerar())
print(coche.frenar())
print(coche.tocarClaxon())

moto = Motocicleta("Honda", "CBR", 2021)
print(moto.acelerar())
print(moto.frenar())
print(moto.tocarClaxon())

# Producto y sus subclases
camisa = Ropa("Camisa", 20, 3, "M", 10)
print(camisa.costoTotal())

pan = Alimento("Pan", 1.5, 10, "2024-12-31")
print(pan.costoTotal())

# Persona y sus subclases
profe = Profesor("Luis", 35, "Hombre", "Matemáticas")
print(profe.informacion())
print(profe.enseñar())

estudiante = Estudiante("Marta", 20, "Mujer", 2)
print(estudiante.informacion())
print(estudiante.estudiar())

director = Director("Ana", 50, "Mujer", "IES Central")
print(director.informacion())
print(director.supervisar())

# Figura y sus subclases
triangulo = Triangulo("Rojo", "Triángulo", 5, 10, 7)
print("Área del Triángulo:", triangulo.calcularArea())
print("Perímetro del Triángulo:", triangulo.calcularPerimetro())

cuadrado = Cuadrado("Azul", "Cuadrado", 4)
print("Área del Cuadrado:", cuadrado.calcularArea())
print("Perímetro del Cuadrado:", cuadrado.calcularPerimetro())

circulo = Circulo("Verde", "Círculo", 3)
print("Área del Círculo:", circulo.calcularArea())
print("Perímetro del Círculo:", circulo.calcularPerimetro())

# Animal y sus subclases
perro = Perro("Rex", 5)
print(perro.hacerSonido())
print(perro.correr())

gato = Gato("Misha", 3)
print(gato.hacerSonido())
print(gato.aranyar())

pajaro = Pajaro("Piolín", 2)
print(pajaro.hacerSonido())
print(pajaro.volar())

