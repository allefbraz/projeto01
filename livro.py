class Livro:

    def __init__(self, titulo, autor, ano, email, telefone, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.email = email
        self.telefone = telefone
        self.status = status

    def transformar_em_texto(self):
        return (
            f"{self.titulo};{self.autor};{self.ano};"
            f"{self.email};{self.telefone};{self.status}\n"
        )