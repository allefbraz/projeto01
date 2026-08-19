import tkinter as tk
from tkinter import ttk, messagebox
from livro import Livro
from biblioteca import salvar_livro, carregar_livros

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Sistema de Biblioteca")
    janela.geometry("1050x650")

    tk.Label(janela, text="SISTEMA DE BIBLIOTECA", font=("Arial", 20, "bold")).pack(pady=15)
    frame = tk.Frame(janela)
    frame.pack(pady=10)
    tk.Label(frame, text="Título:").grid(row=0, column=0, padx=5, pady=5)
    entrada_titulo = tk.Entry(frame, width=40)
    entrada_titulo.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Autor:").grid(row=1, column=0, padx=5, pady=5)
    entrada_autor = tk.Entry(frame, width=40)
    entrada_autor.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="Ano:").grid(row=2, column=0, padx=5, pady=5)
    entrada_ano = tk.Entry(frame, width=40)
    entrada_ano.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame, text="E-mail:").grid(row=3, column=0, padx=5, pady=5)
    entrada_email = tk.Entry(frame, width=40)
    entrada_email.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame, text="Telefone:").grid(row=4, column=0, padx=5, pady=5)
    entrada_telefone = tk.Entry(frame, width=40)
    entrada_telefone.grid(row=4, column=1, padx=5, pady=5)

    colunas = ("titulo", "autor", "ano", "email", "telefone")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings")

    larguras = {"titulo": 180, "autor": 150, "ano": 70, "email": 180, "telefone": 120}
    for col in colunas:
        tabela.heading(col, text=col.capitalize())
        tabela.column(col, width=larguras[col])

    tabela.pack(pady=20, padx=20)

    for livro in carregar_livros():
        tabela.insert("", "end", values=(livro.titulo, livro.autor, livro.ano, livro.email, livro.telefone))

    def cadastrar():
        titulo = entrada_titulo.get()
        autor = entrada_autor.get()
        ano = entrada_ano.get()
        email = entrada_email.get()
        telefone = entrada_telefone.get()

        if not all([titulo, autor, ano, email, telefone]):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        if not ano.isdigit():
            messagebox.showerror("Erro", "O ano deve ser um número!")
            return

        if "@" not in email:
            messagebox.showerror("Erro", "Digite um e-mail válido!")
            return

        livro = Livro(titulo, autor, ano, email, telefone)
        salvar_livro(livro)

        tabela.insert("", "end", values=(livro.titulo, livro.autor, livro.ano, livro.email, livro.telefone))
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

        for entrada in (entrada_titulo, entrada_autor, entrada_ano, entrada_email, entrada_telefone):
            entrada.delete(0, tk.END)

    # Botões
    tk.Button(janela, text="Cadastrar Livro", width=20, command=cadastrar).pack(pady=5)
    tk.Button(janela, text="Sair", width=20, command=janela.destroy).pack(pady=5)

    janela.mainloop()