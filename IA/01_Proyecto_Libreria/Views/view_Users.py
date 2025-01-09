from Controllers import userController
from Model.User import User
import re


def registerUser():
    print("---------Alta de usuario-----------\n")
    while True:
        name = input("Introduce el nombre del usuario\n")
        if len(name) > 1:
            break
        else:
            print("Nombre demasiado corto.")

    while True:
        surname = input("Introduce el/los apellidos del usuario\n")
        if len(surname) > 1:
            break
        else:
            print("Apellido demasiado corto.")

    while True:

        user_input = int(input("Introduce la edad del usuario\n"))
        try:
            age = int(user_input)
            if age > 0:
                break
            else:
                print("Edad negativa. Introduzca una nueva edad.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero")

    while True:

        dni = input("Introduce el dni del usuario\n")
        if re.match(r"[0-9]{8}[A-Za-z]$", dni):
            break
        else:
            print("Dni Inválido")

    while True:
        email = input("Introduce el email del usuario\n")
        if re.match(r"[a-zA-Z!.]@[a-zA-Z].[a-zA-Z]{2,3}", email):
            break
        else:
            print("Email inválido")

    while True:
        address = input("Introduce la dirección del usuario\n")
        if len(address) > 1:
            break
        else:
            print("Dirección demasiado corta")

    while True:

        user_input = int(input("Introduce el número de teléfono del usuario\n"))
        try:
            phone = int(user_input)
            if phone < 100000000:
                print("Número no reconocido")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    user = User()
    user.create(name, surname, dni, email, phone, address, age)
    return userController.register_user(user)


def downUser():
    print("---------Baja de usuario-----------\n")
    dni = input("Introduce el dni del usuario a dar de baja\n")

    user = userController.get_user(dni)
    if user:
        return userController.down_user(user)
    else:
        return "El usuario no existe"


def modUser():
    print("---------Modificación de usuario-----------\n")
    dni = input("Introduce el dni del usuario a modificar\n")

    user = userController.get_user(dni)
    if user:

        while True:
            print("---Menú---")
            print("1. Nombre")
            print("2. Apellidos")
            print("3. Edad")
            print("4. Teléfono")
            print("5. Dirección")

            o = input("")

            if o == "1":
                while True:
                    name = input("Introduce el nombre del usuario\n")
                    if len(name) > 1:
                        break
                    else:
                        print("Nombre inválido")
                return userController.set_name_user(user,name)
            elif o == "2":
                while True:
                    surname = input("Introduce el/los apellidos del usuario\n")
                    if len(surname) > 1:
                        break
                    else:
                        print("Apellido demasiado corto.")

                return userController.set_surname_user(user,surname)
            elif o == "3":
                while True:

                    user_input = int(input("Introduce la edad del usuario\n"))
                    try:
                        age = int(user_input)
                        if age > 0:
                            break
                        else:
                            print("Edad negativa. Introduzca una nueva edad.")
                    except ValueError:
                        print("Entrada inválida. Por favor, introduce un número entero")

                return userController.set_age_user(user,age)
            elif o == "4":
                while True:
                    user_input = int(input("Introduce el número de teléfono del usuario\n"))
                    try:
                        phone = int(user_input)
                        if phone < 100000000:
                            print("Número no reconocido")
                        else:
                            break
                    except ValueError:
                        print("Entrada inválida. Por favor, introduce un número entero.")
                return userController.set_phone_user(user,phone)
            elif o == "5":
                while True:
                    address = input("Introduce la dirección del usuario\n")
                    if len(address) > 1:
                        break
                    else:
                        print("Dirección demasiado corta")
                return userController.set_address_user(user,address)
            else:
                print("Opción no reconocida")
    else:
        return "Usuario no encontrado"

def listUser():
    return userController.list_user()