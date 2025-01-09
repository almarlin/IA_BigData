class Pelota:
    def __init__(self, tipo_de_deporte, tamaño, presion_aire):
        self.tipo_de_deporte = tipo_de_deporte
        self.tamaño = tamaño
        self.presion_aire = presion_aire

    def inflar(self, cantidad):
        self.presion_aire += cantidad
        print(f"Se ha inflado la pelota. La presión de aire ahora es {self.presion_aire} psi.")

    def desinflar(self, cantidad):
        if self.presion_aire - cantidad >= 0:
            self.presion_aire -= cantidad
            print(f"Se ha desinflado la pelota. La presión de aire ahora es {self.presion_aire} psi.")
        else:
            print("No se puede desinflar más. La presión de aire es demasiado baja.")

    def mostrar_estado_presion(self):
        if self.presion_aire < 10:
            estado = "baja"
        elif 10 <= self.presion_aire <= 20:
            estado = "normal"
        else:
            estado = "alta"
        print(f"La presión de aire de la pelota es {estado}.")
        

pelota1 = Pelota("Fútbol", "Mediana", 12)

pelota1.mostrar_estado_presion()

pelota1.inflar(5) 

pelota1.mostrar_estado_presion()

pelota1.desinflar(10)  

pelota1.mostrar_estado_presion()

pelota1.desinflar(10)
