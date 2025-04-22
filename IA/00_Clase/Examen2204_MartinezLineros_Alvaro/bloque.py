import hashlib


class Bloque:
    def __init__(self, id, emisor, receptor, mensaje, hash_anterior=""):
        self.mensaje = mensaje
        self.id = id
        self.emisor = emisor
        self.receptor = receptor
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        self.mensaje = str(self.mensaje)
        contenido = self.mensaje + self.hash_anterior
        return hashlib.sha256(contenido.encode()).hexdigest()
    
    def to_string(self):
        return f"{self.id}, {self.hash},{self.hash_anterior},{self.emisor},{self.receptor},{self.mensaje}"
