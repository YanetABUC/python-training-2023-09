class Libro:
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor

    def __del__(self):
        print(f"El libro {self.titulo} de {self.autor} fue destruido")

libro = Libro("Mi libro imaginario", "Yanet")
del libro