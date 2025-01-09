from Model.Book import Book
import pandas as pd
import os

bookPath="./Data/biblioLibros.csv"
# Params: title(String)
# Se devuelve el libro del fichero encontrado por su titulo
def get_book(title):
    if os.path.getsize(bookPath) > 0:
        old = pd.read_csv(bookPath)

        # Se busca el libro
        d = old[old["title"] == title]

        if d.empty:
            return False
        else:
            # Se convierte a objeto Book
            book = Book()

            data = d.values.tolist()
            book.create(
                data[0][1],
                data[0][2],
                data[0][3],
                data[0][4],
                data[0][5],
                data[0][6],
                data[0][8],
                data[0][7],
            )
            book.id = data[0][0]

            return book
    return False


# Params: book(Book)
# Se registra un libro en el fichero
def register_book(book):
    df = pd.DataFrame([book.to_dict()])
    if os.path.getsize(bookPath) > 0:
        old = pd.read_csv(bookPath)

        d = old[old["title"] == book.title]

        # Si no se encuentra el libro, se añade al dataframe
        if d.empty:
            all = pd.concat([old, df], ignore_index=True)
        # Si se encuentra se modifica la cantidad
        else:
            # Para acceder a los datos del dataframe y modificarlos
            old.loc[old["title"] == book.title, "quantity"] += book.qty

            all = old
        # Se escribe en el fichero
        all.to_csv(bookPath, sep=",", encoding="utf-8", index=False)
    else:
        df.to_csv(bookPath, sep=",", encoding="utf-8", index=False)
    return "Libro registrado correctamente"

# Params: book(Book)
# Se da de baja un libro. Se cambia su disponibilidad a False
def down_book(book):

    book.available = False

    if os.path.getsize(bookPath) > 0:
        old = pd.read_csv(bookPath)

        # Se busca el libro
        d = old[old["id"] == book.id]

        if d.empty:
            return "No hay libros registrados"
        else:
            # Campo disponibilidad a False
            old.loc[old["id"] == book.id, "available"] = False
            all = old
        # Se escribe en el fichero
        all.to_csv(bookPath, sep=",", encoding="utf-8", index=False)

        return "Libro dado de baja"

# Params: book(Book)
# Se da de alta un libro ya registrado. Se cambia su disponibilidad a True
def up_book(book):
    book.available = True

    if os.path.getsize(bookPath) > 0:
        old = pd.read_csv(bookPath)

        # Se busca el libro
        d = old[old["id"] == book.id]

        if d.empty:
            return "No hay libros registrados"
        else:
            # Campo disponibilidad a True
            old.loc[old["id"] == book.id, "available"] = True
            all = old
        # Se escribe en el fichero
        all.to_csv(bookPath, sep=",", encoding="utf-8", index=False)

        return "Libro dado de alta"

def save_book(book):
    bookDf = pd.DataFrame([book.to_dict()])

    if os.path.getsize(bookPath) > 0:

        old = pd.read_csv(bookPath)
        bookDf = bookDf.astype(old.dtypes.to_dict())

        # Modificamos el dataframe
        old.update(old[["id"]].merge(bookDf,'right'))

        # Se escribe en el fichero
        old.to_csv(bookPath, sep=",", encoding="utf-8", index=False)
    
    return "Libro actualizado"

def set_title_book(book,title):
    book.title = title
    return save_book(book)

def set_year_book(book,year):
    book.year = year
    return save_book(book)

def set_pages_book(book,pages):
    book.pages = pages
    return save_book(book)

def set_genre_book(book,genre):
    book.genre = genre
    return save_book(book)

def set_publisher_book(book,publisher):
    book.publisher = publisher
    return save_book(book)

def set_state_book(book,state):
    book.state = state
    return save_book(book)

def set_qty_book(book,qty):
    book.qty = qty
    return save_book(book)

def list_books():
    if os.path.getsize(bookPath) > 0:
        old = pd.read_csv(bookPath)

        return old