from typing import final
class Empleado():

    def __init__(self, nombre, sueldo, empresa):
        self.nombre = nombre
        self.sueldo = sueldo
        self.num = 0
        for i,e in enumerate(empresa.empleados):
            if e == 'None':
                self.num = i
        if self.num == 0:
            self.num = empresa.tamanyo + 1
            empresa.tamanyo += 1

    @final
    def aumentar_sueldo(self,porce) :
        self.sueldo +=  self.sueldo * (porce/100)
        
    def despedir(self, empresa):
        for e in empresa.empleados:
            if e == self:
                empresa.empleados.remove(e)
                self.num = 0
                break
    
    def get_nombre(self):
        return self.nombre
    
    def get_sueldo(self):
        return self.sueldo
    
    def get_num_empleado(self):
        return self.num
    
    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def set_sueldo(self,sueldo):
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado número: {self.num} : {self.nombre} : Sueldo: {self.sueldo}"
    


