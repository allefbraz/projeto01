from livro import Livro
NOME_ARQUIVO = "livros.txt"
def salvar_livro(livro):
    with open(NOME_ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(livro.transformar_em_texto())
def carregar_livros():
    livros = []
    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 5:
                    livros.append(Livro(*dados))
    except FileNotFoundError:
        open(NOME_ARQUIVO, "w").close()
    return livros