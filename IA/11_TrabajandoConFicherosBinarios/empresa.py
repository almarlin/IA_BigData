from empleado import Empleado
import pickle
class Empresa():

    def __init__(self, nombre, tamanyo):
        self.nombre = nombre
        self.tamanyo = tamanyo
        self.empleados = ['None'] * tamanyo

        try:
            with open('MisEmpleados.dat', 'rb') as file:
                self.empleados = pickle.load(file)
                self.tamanyo = len(self.empleados)
        except FileNotFoundError:
            print("Archivo 'MisEmpleados.dat' no encontrado. Se creará uno nuevo.")
    
    def get_nombre(self):
        return self.nombre
    
    def get_tamanyo(self):
        return self.tamanyo
    
    def get_empleado(self, index):
        if index > self.tamanyo:
            return False
        else:
            return self.empleados[index]

    def despedir_empleado(self, index):
        for i, empleado in enumerate(self.empleados):
            if empleado == index:
                self.empleados[i] = 'None'
                print(f"Empleado {index.nombre} reemplazado por 'None'.")
                break
            
    def nuevo_empleado(self, nombre,sueldo):
        empl = Empleado(nombre,sueldo,self)
        self.empleados.append(empl)

        with open('MisEmpleados.dat', 'wb') as file:
            pickle.dump(self.empleados, file)
            print("Datos de empleados guardados en 'MisEmpleados.dat'.")

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)
