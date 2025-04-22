from bloque import Bloque
import json 

class Blockchain:
    def __init__(self):
        self.cadena = [self.crear_bloque_genesis()]
 
    def crear_bloque_genesis(self):
        return Bloque(0, emisor="GENESIS", receptor="TODOS", mensaje="Inicio de la cadena", hash_anterior="0")
 
    # Añadimos emisor y receptor
    def agregar_bloque(self, emisor, receptor, mensaje):
        ultimo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), emisor, receptor, mensaje, ultimo_bloque.hash)
        self.cadena.append(nuevo_bloque)
 
    def es_valida(self):
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]
 
            if bloque_actual.hash != bloque_actual.calcular_hash():
                return {"valida":False,"bloque":bloque_actual.id}
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return {"valida":False,"bloque":bloque_anterior.id}
        return {"valida":True,"bloque":"N/A"}
 
    def mostrar_transacciones(self):
        for bloque in self.cadena[1:]:  # omitimos el bloque génesis
            print(f"{bloque.id} | Hash: {bloque.hash}| {bloque.emisor} → {bloque.receptor}: {bloque.mensaje} | Hash anterior: {bloque.hash_anterior}")
 
    
    def reparar(self,idReparar):
        for i in range(idReparar, len(self.cadena)):
            bloqueActual = self.cadena[i]
            
            if i == 0:  # Bloque génesis (primer bloque)
                bloqueActual.hash_anterior = "0"  # Siempre será 0 en el bloque génesis
            else:
                bloqueAnterior = self.cadena[i-1]
                bloqueActual.hash_anterior = bloqueAnterior.hash  # El hash anterior se actualiza
            
            bloqueActual.hash = bloqueActual.calcular_hash()  # Recalculamos el hash del bloque actual
    
    def to_txt(self):
        datos = [bloque.to_string() for bloque in self.cadena]
        with open("blockchain_backup.txt", 'w') as f:
            json.dump(datos, f, indent=4)
        