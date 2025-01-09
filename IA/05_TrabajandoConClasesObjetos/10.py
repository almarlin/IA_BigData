class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def ajustar_hora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def avanzar_segundo(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.avanzar_minuto()

    def avanzar_minuto(self):
        self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.avanzar_hora()

    def avanzar_hora(self):
        self.hora += 1
        if self.hora == 24:
            self.hora = 0

    def mostrar_hora(self):
        print(f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}")


reloj1 = Reloj(12, 30, 45)

reloj1.mostrar_hora()
reloj1.avanzar_segundo()
reloj1.mostrar_hora()
reloj1.avanzar_minuto()
reloj1.mostrar_hora()
reloj1.ajustar_hora(23, 59, 55)
reloj1.mostrar_hora()
reloj1.avanzar_segundo()
reloj1.mostrar_hora()
