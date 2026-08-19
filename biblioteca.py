from livro import Livro

NOME_ARQUIVO = "livros.txt"
ARQUIVO_EMPRESTIMOS = "emprestimos.txt"


def salvar_livro(livro):
    with open(NOME_ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(livro.transformar_em_texto())


def carregar_livros():
    livros = []

    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                dados = linha.strip().split(";")

                if len(dados) == 5:
                    livros.append(Livro(*dados))

                elif len(dados) == 6:
                    livros.append(Livro(*dados))

    except FileNotFoundError:
        open(NOME_ARQUIVO, "w", encoding="utf-8").close()

    return livros


def salvar_todos_livros(livros):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
        for livro in livros:
            arquivo.write(livro.transformar_em_texto())


def excluir_livro(livro):
    livros = carregar_livros()

    livros = [
        item for item in livros
        if not (
            item.titulo == livro.titulo
            and item.autor == livro.autor
            and item.ano == livro.ano
            and item.email == livro.email
            and item.telefone == livro.telefone
        )
    ]

    salvar_todos_livros(livros)


def registrar_emprestimo(livro, leitor):
    with open(ARQUIVO_EMPRESTIMOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{livro.titulo};{leitor};EMPRESTADO\n"
        )


def registrar_devolucao(livro, leitor):
    with open(ARQUIVO_EMPRESTIMOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{livro.titulo};{leitor};DEVOLVIDO\n"
        )


def carregar_historico():
    historico = []

    try:
        with open(ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                dados = linha.strip().split(";")

                if len(dados) == 3:
                    historico.append(dados)

    except FileNotFoundError:
        open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8").close()

    return historico