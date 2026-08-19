import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from livro import Livro
from biblioteca import (
    salvar_livro,
    carregar_livros,
    salvar_todos_livros,
    excluir_livro,
    registrar_emprestimo,
    registrar_devolucao,
    carregar_historico
)


def iniciar_interface():

    janela = tk.Tk()
    janela.title("Sistema de Biblioteca")
    janela.geometry("1100x700")


    tk.Label(
        janela,
        text="SISTEMA DE BIBLIOTECA",
        font=("Arial", 32, "bold")
    ).pack(pady=15)


    frame = tk.Frame(janela)
    frame.pack(pady=5)

    tk.Label(frame, text="Título:").grid(
        row=0, column=0, padx=5, pady=5
    )

    entrada_titulo = tk.Entry(frame, width=40)
    entrada_titulo.grid(
        row=0, column=1, padx=5, pady=5
    )

    tk.Label(frame, text="Autor:").grid(
        row=1, column=0, padx=5, pady=5
    )

    entrada_autor = tk.Entry(frame, width=40)
    entrada_autor.grid(
        row=1, column=1, padx=5, pady=5
    )

    tk.Label(frame, text="Ano:").grid(
        row=2, column=0, padx=5, pady=5
    )

    entrada_ano = tk.Entry(frame, width=40)
    entrada_ano.grid(
        row=2, column=1, padx=5, pady=5
    )

    tk.Label(frame, text="E-mail:").grid(
        row=3, column=0, padx=5, pady=5
    )

    entrada_email = tk.Entry(frame, width=40)
    entrada_email.grid(
        row=3, column=1, padx=5, pady=5
    )

    tk.Label(frame, text="Telefone:").grid(
        row=4, column=0, padx=5, pady=5
    )

    entrada_telefone = tk.Entry(frame, width=40)
    entrada_telefone.grid(
        row=4, column=1, padx=5, pady=5
    )



    frame_pesquisa = tk.Frame(janela)
    frame_pesquisa.pack(pady=10)

    tk.Label(
        frame_pesquisa,
        text="Pesquisar:"
    ).pack(side=tk.LEFT, padx=5)

    entrada_pesquisa = tk.Entry(
        frame_pesquisa,
        width=35
    )
    entrada_pesquisa.pack(side=tk.LEFT, padx=5)


    colunas = (
        "titulo",
        "autor",
        "ano",
        "email",
        "telefone",
        "status"
    )

    tabela = ttk.Treeview(
        janela,
        columns=colunas,
        show="headings",
        height=12
    )

    larguras = {
        "titulo": 180,
        "autor": 150,
        "ano": 60,
        "email": 180,
        "telefone": 120,
        "status": 110
    }

    for coluna in colunas:

        tabela.heading(
            coluna,
            text=coluna.capitalize()
        )

        tabela.column(
            coluna,
            width=larguras[coluna]
        )

    tabela.pack(
        pady=10,
        padx=20
    )



    def limpar_campos():

        for entrada in (
            entrada_titulo,
            entrada_autor,
            entrada_ano,
            entrada_email,
            entrada_telefone
        ):
            entrada.delete(0, tk.END)

    def atualizar_tabela(lista=None):

        for item in tabela.get_children():
            tabela.delete(item)

        if lista is None:
            lista = carregar_livros()

        for livro in lista:

            tabela.insert(
                "",
                "end",
                values=(
                    livro.titulo,
                    livro.autor,
                    livro.ano,
                    livro.email,
                    livro.telefone,
                    livro.status
                )
            )

    def obter_livro_selecionado():

        selecionado = tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Aviso",
                "Selecione um livro na tabela!"
            )
            return None

        valores = tabela.item(
            selecionado[0],
            "values"
        )

        return Livro(*valores)



    def cadastrar():

        titulo = entrada_titulo.get().strip()
        autor = entrada_autor.get().strip()
        ano = entrada_ano.get().strip()
        email = entrada_email.get().strip()
        telefone = entrada_telefone.get().strip()

        if not all([
            titulo,
            autor,
            ano,
            email,
            telefone
        ]):
            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )
            return

        if not ano.isdigit():

            messagebox.showerror(
                "Erro",
                "O ano deve ser um número!"
            )

            return

        if "@" not in email:

            messagebox.showerror(
                "Erro",
                "Digite um e-mail válido!"
            )

            return

        livro = Livro(
            titulo,
            autor,
            ano,
            email,
            telefone
        )

        salvar_livro(livro)

        atualizar_tabela()

        limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Livro cadastrado com sucesso!"
        )



    def editar():

        livro_antigo = obter_livro_selecionado()

        if livro_antigo is None:
            return

        entrada_titulo.delete(0, tk.END)
        entrada_titulo.insert(0, livro_antigo.titulo)

        entrada_autor.delete(0, tk.END)
        entrada_autor.insert(0, livro_antigo.autor)

        entrada_ano.delete(0, tk.END)
        entrada_ano.insert(0, livro_antigo.ano)

        entrada_email.delete(0, tk.END)
        entrada_email.insert(0, livro_antigo.email)

        entrada_telefone.delete(0, tk.END)
        entrada_telefone.insert(0, livro_antigo.telefone)

        def salvar_edicao():

            titulo = entrada_titulo.get().strip()
            autor = entrada_autor.get().strip()
            ano = entrada_ano.get().strip()
            email = entrada_email.get().strip()
            telefone = entrada_telefone.get().strip()

            if not all([
                titulo,
                autor,
                ano,
                email,
                telefone
            ]):

                messagebox.showerror(
                    "Erro",
                    "Preencha todos os campos!"
                )

                return

            if not ano.isdigit():

                messagebox.showerror(
                    "Erro",
                    "O ano deve ser um número!"
                )

                return

            if "@" not in email:

                messagebox.showerror(
                    "Erro",
                    "Digite um e-mail válido!"
                )

                return

            livros = carregar_livros()

            for livro in livros:

                if (
                    livro.titulo == livro_antigo.titulo
                    and livro.autor == livro_antigo.autor
                    and livro.ano == livro_antigo.ano
                    and livro.email == livro_antigo.email
                    and livro.telefone == livro_antigo.telefone
                ):

                    livro.titulo = titulo
                    livro.autor = autor
                    livro.ano = ano
                    livro.email = email
                    livro.telefone = telefone

                    break

            salvar_todos_livros(livros)

            atualizar_tabela()

            limpar_campos()

            botao_salvar_edicao.destroy()

            messagebox.showinfo(
                "Sucesso",
                "Livro alterado com sucesso!"
            )

        botao_salvar_edicao = tk.Button(
            janela,
            text="Salvar Alterações",
            width=18,
            command=salvar_edicao
        )

        botao_salvar_edicao.pack(pady=3)



    def excluir():

        livro = obter_livro_selecionado()

        if livro is None:
            return

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f'Deseja excluir o livro "{livro.titulo}"?'
        )

        if not confirmar:
            return

        excluir_livro(livro)

        atualizar_tabela()

        messagebox.showinfo(
            "Sucesso",
            "Livro excluído com sucesso!"
        )



    def pesquisar():

        termo = entrada_pesquisa.get().strip().lower()

        livros = carregar_livros()

        if not termo:

            atualizar_tabela(livros)
            return

        resultado = []

        for livro in livros:

            if (
                termo in livro.titulo.lower()
                or termo in livro.autor.lower()
                or termo in livro.ano.lower()
                or termo in livro.email.lower()
                or termo in livro.telefone.lower()
                or termo in livro.status.lower()
            ):

                resultado.append(livro)

        atualizar_tabela(resultado)

    def limpar_pesquisa():

        entrada_pesquisa.delete(
            0,
            tk.END
        )

        atualizar_tabela()


    def emprestar():

        livro = obter_livro_selecionado()

        if livro is None:
            return

        if livro.status == "Emprestado":

            messagebox.showwarning(
                "Aviso",
                "Este livro já está emprestado!"
            )

            return

        leitor = simpledialog.askstring(
            "Empréstimo",
            "Nome do leitor:"
        )

        if not leitor:
            return

        livros = carregar_livros()

        for item in livros:

            if (
                item.titulo == livro.titulo
                and item.autor == livro.autor
                and item.ano == livro.ano
                and item.email == livro.email
                and item.telefone == livro.telefone
            ):

                item.status = "Emprestado"
                break

        salvar_todos_livros(livros)

        registrar_emprestimo(
            livro,
            leitor
        )

        atualizar_tabela()

        messagebox.showinfo(
            "Sucesso",
            f'Livro emprestado para {leitor}.'
        )



    def devolver():

        livro = obter_livro_selecionado()

        if livro is None:
            return

        if livro.status == "Disponível":

            messagebox.showwarning(
                "Aviso",
                "Este livro já está disponível!"
            )

            return

        leitor = simpledialog.askstring(
            "Devolução",
            "Nome do leitor:"
        )

        if not leitor:
            return

        livros = carregar_livros()

        for item in livros:

            if (
                item.titulo == livro.titulo
                and item.autor == livro.autor
                and item.ano == livro.ano
                and item.email == livro.email
                and item.telefone == livro.telefone
            ):

                item.status = "Disponível"
                break

        salvar_todos_livros(livros)

        registrar_devolucao(
            livro,
            leitor
        )

        atualizar_tabela()

        messagebox.showinfo(
            "Sucesso",
            f'Livro devolvido por {leitor}.'
        )


    def abrir_historico():

        janela_historico = tk.Toplevel(janela)

        janela_historico.title(
            "Histórico de Empréstimos"
        )

        janela_historico.geometry(
            "700x400"
        )

        tk.Label(
            janela_historico,
            text="HISTÓRICO DE EMPRÉSTIMOS",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        colunas_historico = (
            "livro",
            "leitor",
            "acao"
        )

        tabela_historico = ttk.Treeview(
            janela_historico,
            columns=colunas_historico,
            show="headings"
        )

        tabela_historico.heading(
            "livro",
            text="Livro"
        )

        tabela_historico.heading(
            "leitor",
            text="Leitor"
        )

        tabela_historico.heading(
            "acao",
            text="Ação"
        )

        tabela_historico.column(
            "livro",
            width=300
        )

        tabela_historico.column(
            "leitor",
            width=200
        )

        tabela_historico.column(
            "acao",
            width=120
        )

        tabela_historico.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        for registro in carregar_historico():

            tabela_historico.insert(
                "",
                "end",
                values=(
                    registro[0],
                    registro[1],
                    registro[2]
                )
            )


    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=5)

    tk.Button(
        frame_botoes,
        text="Cadastrar Livro",
        width=18,
        command=cadastrar
    ).grid(row=0, column=0, padx=3)

    tk.Button(
        frame_botoes,
        text="Editar",
        width=18,
        command=editar
    ).grid(row=0, column=1, padx=3)

    tk.Button(
        frame_botoes,
        text="Excluir",
        width=18,
        command=excluir
    ).grid(row=0, column=2, padx=3)

    tk.Button(
        frame_botoes,
        text="Emprestar",
        width=18,
        command=emprestar
    ).grid(row=1, column=0, padx=3, pady=5)

    tk.Button(
        frame_botoes,
        text="Devolver",
        width=18,
        command=devolver
    ).grid(row=1, column=1, padx=3, pady=5)

    tk.Button(
        frame_botoes,
        text="Histórico",
        width=18,
        command=abrir_historico
    ).grid(row=1, column=2, padx=3, pady=5)

    tk.Button(
        frame_pesquisa,
        text="Pesquisar",
        command=pesquisar
    ).pack(side=tk.LEFT, padx=3)

    tk.Button(
        frame_pesquisa,
        text="Limpar",
        command=limpar_pesquisa
    ).pack(side=tk.LEFT, padx=3)

    tk.Button(
        janela,
        text="Sair",
        width=58,
        bg="red",
        fg="white",
        command=janela.destroy
    ).pack(pady=5)


    atualizar_tabela()

    janela.mainloop()