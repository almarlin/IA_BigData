class Mascota:
    def __init__(self, nombre, tipo_animal, edad, energia):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.edad = edad
        self.energia = energia

    def alimentar(self, cantidad):
        self.energia += cantidad
        if self.energia > 100:
            self.energia = 100

    def jugar(self, tiempo):
        self.energia -= tiempo * 2
        if self.energia < 0:
            self.energia = 0

    def mostrar_energia(self):
        if self.energia > 70:
            estado = "llena de energía"
        elif self.energia < 30:
            estado = "cansada"
        else:
            estado = "energía normal"
        print(f"{self.nombre} está {estado} con {self.energia}% de energía.")


mascota1 = Mascota("Max", "Perro", 3, 50)

mascota1.mostrar_energia()
mascota1.alimentar(30)
mascota1.mostrar_energia()
mascota1.jugar(10)
mascota1.mostrar_energia()
