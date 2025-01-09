class CuentaBancaria:
    def __init__(self, titular, saldo, tipo):
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo
    def deposit(self,cant):
        if cant > 0:
            self.saldo+=cant
            return f"El saldo asciende a {self.saldo}"
        else:
            return "No se pueden depositar cantidades negativas."
        
    def draw(self,cant):
        if self.saldo >= cant:
            if cant < 0:
                self.saldo+=cant
                return f"El saldo asciende a {self.saldo}"
            else:
                self.saldo-=cant
                return f"El saldo asciende a {self.saldo}"
        else:
            return "Cantidad a retirar mayor que el saldo disponible"
    
    def show(self):
        return f"El saldo asciende a {self.saldo}"
    
cuenta = CuentaBancaria("Álvaro",5000,"Ahorros")

print(cuenta.show())

print(cuenta.deposit(500))
print(cuenta.draw(1500))
print(cuenta.draw(4500))
