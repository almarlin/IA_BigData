class Libro:
    def __init__(self, titulo, autor, paginas, editorial, anyo):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.anyo = anyo

    def mostrar(self):
        libro = {
            "Titulo": self.titulo,
            "Autor":self.autor,
            "Páginas":self.paginas,
            "Editorial":self.editorial,
            "Año":self.anyo
        }
        return libro
    def mayor(self):
        if self.paginas > 300:
            largo = "grande"
        else:
            largo = "pequeño"
        return largo
    
libro = Libro("Dune","Frank Herbert",761,"Debolsillo",2021)

print(f"{libro.mostrar()} || El libro es {libro.mayor()}")

