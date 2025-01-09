class Smartphone:
    def __init__(self, marca, modelo, memoria, bateria, nivel_bateria):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.bateria = bateria
        self.nivel_bateria = nivel_bateria

    def llamar(self, duracion_llamada):
        self.nivel_bateria -= duracion_llamada * 0.5
        if self.nivel_bateria < 0:
            self.nivel_bateria = 0

    def cargar(self, cantidad):
        self.nivel_bateria += cantidad
        if self.nivel_bateria > self.bateria:
            self.nivel_bateria = self.bateria

    def mostrar_nivel_bateria(self):
        print(f"Nivel de batería actual: {self.nivel_bateria}%")


smartphone1 = Smartphone("Samsung", "Galaxy S21", "128GB", 100, 50)

smartphone1.mostrar_nivel_bateria()
smartphone1.llamar(30)
smartphone1.mostrar_nivel_bateria()
smartphone1.cargar(20)
smartphone1.mostrar_nivel_bateria()
