from Controllers import lendingController,userController,bookController
from Model.Lending import Lending

def createLend():

    print("------Creando un préstamo------\n")

    userDni = input("Introduce el dni del usuario\n")
    user = userController.get_user(userDni)
    if user == False:
        return "No se ha encontrado el usuario"
    
    bookTitle = input("Introduce el título del libro\n")
    book = bookController.get_book(bookTitle)

    if book == False:
        return "Libro no registrado en el sistema\n"
    
    return lendingController.lend_book_to_user(book,user)

def returnLend():
    print("------Devolviendo un préstamo------\n")
    userDni = input("Introduce el dni del usuario\n")
    user = userController.get_user(userDni)
    
    if user == False:
        return "No se ha encontrado el usuario\n"
    
    bookTitle = input("Introduce el título del libro\n")
    book = bookController.get_book(bookTitle)

    if book == False:
        return "Libro no registrado en el sistema\n"
    
    return lendingController.return_book(book,user)

def listLendUser():
    print("------Lista de préstamos de un usuario------\n")

    userDni = input("Introduce el dni del usuario\n")
    user = userController.get_user(userDni)
    if user == False:
        return "No se ha encontrado el usuario"
    
    return lendingController.get_pending_lends(user)

def listLends():
    print("------Lista de préstamos pendientes------\n")
    
    return lendingController.get_pending_lends()