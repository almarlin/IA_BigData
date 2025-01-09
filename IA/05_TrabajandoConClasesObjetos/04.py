class Cafetera:
    def __init__(self, marca, maxCap, nvlAct):
        self.marca = marca
        self.maxCap = maxCap
        self.nvlAct = nvlAct
    
    def servir(self,cafes):
        if cafes * 0.1 < self.nvlAct:
            self.nvlAct -= cafes * 0.1
            return f"Cafetera a {self.nvlAct} L. {cafes * 100} ml servidos."
        else:
            return f"No se pueden servir tantos cafés."
    
    def rellenar(self):
        self.nvlAct = self.maxCap
        return "Cafetera llena."
    
    def vaciaOLlena(self):
        if self.nvlAct == 0:
            return "Cafetera vacía"
        elif self.nvlAct == self.maxCap:
            return "Cafetera llena"
        else:
            return f"Cafetera al { 100 - self.nvlAct * self.maxCap } %"
        
cafetera = Cafetera("Delonghi", 5, 0)

print(cafetera.vaciaOLlena())
print(cafetera.rellenar())
print(cafetera.servir(7))
print(cafetera.vaciaOLlena())