import pandas as pd
import os

bookPath = "./Data/biblioLibros.csv"

class Book:
    def __init__(self):
        if os.path.exists(bookPath) and os.path.getsize(bookPath) > 0:
            books = pd.read_csv(bookPath)
            self.id = books["id"].iloc[-1] + 1
        else:
            self.id = 1
        
    def create(self, title, year, pages, genre, publisher, state,qty,*available):

        self.title = title
        self.year = year
        self.pages = pages
        self.genre = genre
        self.publisher = publisher
        self.state = state

        # Available llega como un parámetro opcional, que se interpretan como listas. La primera posición recoge el valor de disponibilidad del libro
        if available:
            self.available = available[0]
        else:
            self.available = True

        self.qty = qty
        return self

    def __str__(self):
        return f"\n-----------------------\nINFORMACIÓN DEL LIBRO\n-----------------------\nID: {self.id} \nTitulo: {self.title} \nAño: {self.year} \nPáginas: {self.pages}\nGénero: {self.genre} \nEditorial: {self.publisher} \nEstado: {self.state}\nDisponibilidad: {self.available} \nCantidad: {self.qty}\n"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "pages": self.pages,
            "genre": self.genre,
            "publisher": self.publisher,
            "state": self.state,
            "available": self.available,
            "quantity": self.qty
        }