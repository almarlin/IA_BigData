import pandas as pd
import os

userPath = "./Data/biblioUsuarios.csv"

class User:
    def __init__(self):        
                
        if os.path.exists(userPath) and os.path.getsize(userPath) > 0:
            users = pd.read_csv(userPath)
            self.id = users["id"].iloc[-1] + 1
        else:
            self.id = 1


    def create(self, name, surname, dni, email, phone, address, age):

        self.name = name
        self.surname = surname
        self.dni = dni
        self.email = email
        self.phone = phone
        self.address = address
        self.age = age


    def __str__(self):
        return f"\n-----------------------\nINFORMACIÓN DEL USUARIO\n-----------------------\nID: {self.id} \nNombre: {self.name} \nApellidos: {self.surname}\nEdad: {self.age} \nDNI: {self.dni}\nEmail: {self.email} \nTeléfono: {self.phone} \nDirección: {self.address}\n"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "dni": self.dni,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "age": self.age
        }