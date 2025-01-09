from Model import *
from Views import view_Books,view_Users,view_Lendings

# Método principal
def main():
    print(f"\n--------------------------------------------")
    print(f"                Biblioteca                  ")
    print(f"--------------------------------------------\n")
    while True:

        print(f"--------Menú-------")
        print(f"0. Salir del sistema")
        print(f"1. Libros")
        print(f"2. Usuarios")
        print(f"3. Préstamos")
        o = int(input(""))
        
        if o == 0:
            print(f"Saliendo del sistema.")
            break
        elif o == 1:
            gestionLibros()
        elif o == 2:
            gestionUsuarios()
            pass
        elif o == 3:
            gestionPrestamos()
            pass
        else:
            print(f"Opción no registrada. Ingrese una de nuevo.")

def gestionLibros():
    while True:

        print(f"-------Libros------")
        print(f"0. Salir")
        print(f"1. Dar de alta un libro")
        print(f"2. Dar de baja un libro")
        print(f"3. Modificar los datos de un libro")
        print(f"4. Listado general de los libros")
        o = input("")
        
        if o == "0":
            print(f"Saliendo...\n")
            break
        elif o == "1":
            print("0. Salir")
            print("1. Libro nuevo")
            print("2. Libro registrado")
            o2 = input("")

            while True:
                if o2 == "1":
                    print(f"{view_Books.registerBook()}")
                    break
                elif o2 == "2":
                    print(f"{view_Books.upBook()}")
                    break
                elif o2 == "0":
                    break
                else:
                    print("Introduce una opción válida")

        elif o == "2":
            print(f"{view_Books.downBook()}\n")
            pass
        elif o == "3":
            print(f"{view_Books.modBook()}\n")
            pass
        elif o == "4":
            print(f"{view_Books.listBook()}\n")
            pass
        else:
            print(f"Opción no registrada. Ingrese una de nuevo.")

def gestionUsuarios():
    while True:

        print(f"-------Usuarios------")
        print(f"0. Salir")
        print(f"1. Dar de alta un usuario")
        print(f"2. Dar de baja un usuario")
        print(f"3. Modificar los datos de un usuario")
        print(f"4. Listado general de los usuarios")
        o = input("")
        
        if o == "0":
            print(f"Saliendo...\n")
            break
        elif o == "1":
            print(f"{view_Users.registerUser()}")
        elif o == "2":
            print(f"{view_Users.downUser()}\n")
            pass
        elif o == "3":
            print(f"{view_Users.modUser()}\n")
            pass
        elif o == "4":
            print(f"{view_Users.listUser()}\n")
            pass
        else:
            print(f"Opción no registrada. Ingrese una de nuevo.")

def gestionPrestamos():
    while True:

        print(f"-------Prestamos------")
        print(f"0. Salir")
        print(f"1. Registrar un nuevo préstamo")
        print(f"2. Devolución de un préstamo")
        print(f"3. Listar los préstamos pendientes de un usuario")
        print(f"4. Listado general de los préstamos pendientes")
        o = input("")
        
        if o == "0":
            print(f"Saliendo...\n")
            break
        elif o == "1":
            print(f"{view_Lendings.createLend()}")
        elif o == "2":
            print(f"{view_Lendings.returnLend()}\n")
            pass
        elif o == "3":
            print(f"{view_Lendings.listLendUser()}\n")
            pass
        elif o == "4":
            print(f"{view_Lendings.listLends()}\n")
            pass
        else:
            print(f"Opción no registrada. Ingrese una de nuevo.")

main()
