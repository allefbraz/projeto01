class Livro:

    def __init__(self, titulo, autor, ano, email, telefone):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.email = email
        self.telefone = telefone

    def transformar_em_texto(self):
        return (
            f"{self.titulo};{self.autor};{self.ano};{self.email};{self.telefone}\n"
        )