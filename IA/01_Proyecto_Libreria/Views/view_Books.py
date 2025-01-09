from Model.Book import Book
from Controllers import bookController

# Vista de registro de un libro
def registerBook():
    while True:
        title = input("Introduce el título del libro\n")
        if len(title) > 1:
            break
        else:
            print("Título demasiado corto.")

    while True:

        year = int(input("Introduce el año de publicación del libro\n"))
        try:
            number = int(year)
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    while True:

        pages = int(input("Introduce el número de páginas totales del libro\n"))
        try:
            number = int(pages)
            if number > 0:
                break
            else:
                print("No pueden haber páginas negativas")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    while True:
        genre = input("Introduce el género del libro\n")
        if len(genre) > 1:
            break
        else:
            print("Género demasiado corto.")

    while True:
        publisher = input("Introduce la editorial del libro\n")
        if len(publisher) > 1:
            break
        else:
            print("Nombre demasiado corto.")

    while True:

        state = int(
            input(
                "Introduce el estado del libro \n1. Nuevo \n2. Seminuevo \n3. Usado\n"
            )
        )
        try:
            number = int(state)
            if state > 3 or state < 1:
                print("Número no reconocido")
            else:
                if state == 1:
                    bookState = "Nuevo"
                elif state == 2:
                    bookState = "Seminuevo"
                else:
                    bookState="Usado"
                break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    while True:  

        number = input("Introduce cuántos libros son\n")

        try:
            qty = int(number)
            if qty < 0:
                print("Cantidad menor a 0")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")
    
    
    while True:
        user_input = input(
            "Introduce la disponibilidad del libro \nDisponible: 1 \nNo disponible: 0\n"
        )
        if user_input == '1':
            available = True
            break
        elif user_input == '0':
            available = False
            break
        else:
            print("Entrada inválida. Por favor, introduce 1 para disponible o 0 para no disponible.")
            
    book = Book()
    book.create(title,year,pages,genre,publisher,bookState,qty,available)
    bookController.register_book(book)

# Vista de baja de un libro
def downBook():
    while True:
        title = input("Introduce el título del libro a dar de baja\n")
        if len(title) > 1:
            break
        else:
            print("Título demasiado corto.")
    
    book = bookController.get_book(title)
    if book:
        return bookController.down_book(book)
    else:
        return "Libro no encontrado"

# Vista de alta de un libro
def upBook():
    while True:
        title = input("Introduce el título del libro a dar de alta\n")
        if len(title) > 1:
            break
        else:
            print("Título demasiado corto.")
    
    book = bookController.get_book(title)
    if book:
        return bookController.up_book(book)
    else:
        return "Libro no encontrado"

# Vista de modificación de libros
def modBook():
    print("\n---------Modificación de un libro----------")
    while True:
        title = input("Introduce el título del libro a modificar\n")
        if len(title) > 1:
            break
        else:
            print("Título demasiado corto.")
    
    book = bookController.get_book(title)
    if book:
        while True: 
            print(f"\n----------Modificando {book.title}------------")
            print("0. Salir")
            print("1. Titulo")
            print("2. Páginas")
            print("3. Género")
            print("4. Editorial")
            print("5. Estado")
            print("6. Cantidad")
        
            o = input("")
            if o == "0":
                break
            elif o =='1':
                print(f"Título actual: {book.title}")
                title = input("Introduce el nuevo título\n")
                return bookController.set_title_book(book,title)
            elif o == '2':
                print(f"Páginas actuales: {book.pages}")
                user_input = input("Introduce el nuevo número de páginas\n")
                try:
                    pages = int(user_input)
                    if pages < 1:
                        return "Número de páginas inválido"
                    return bookController.set_pages_book(book,pages)
                except:
                    print("Número inválido")                
            elif o == '3':
                print(f"Género actual: {book.genre}")
                genre = input("Introduce el nuevo género\n")
                return bookController.set_genre_book(book,genre)
            elif o == '4':
                print(f"Editorial actual: {book.publisher}")
                publisher = input("Introduce la nueva editorial\n")
                return bookController.set_publisher_book(book,publisher)
            elif o == '5':
                print(f"Estado actual: {book.state}")
                state = input("Introduce la nueva editorial\n")
                return bookController.set_state_book(book,state)
            elif o == '6':
                print(f"Cantidad actual: {book.qty}")
                user_input = input("Introduce el nuevo número de libros\n")
                try:
                    qty = int(user_input)
                    if qty < 1:
                        return "Número de libros inválido"
                    return bookController.set_qty_book(book,qty)
                except:
                    print("Número inválido") 
    else:
        return "Libro no encontrado"
    
# Vista de listado de libros
def listBook():
    return f"---------Listado---------\n{bookController.list_books()}"