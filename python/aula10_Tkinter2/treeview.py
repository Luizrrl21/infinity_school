import tkinter as tk
from tkinter import ttk

# Criar janela
janela = tk.Tk()
janela.title("Exemplo de Treeview")

# Criar Treeview
treeview = ttk.Treeview(janela)

# Adicionar colunas
treeview["columns"] = ("Nome", "Idade", "Cidade")

# Configurar cabeçalhos das colunas
treeview.heading("#0", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Idade", text="Idade")
treeview.heading("Cidade", text="Cidade")

# Adicionar dados
dados1 = ("1", "João", "25", "São Paulo")
dados2 = ("2", "Maria", "30", "Rio de Janeiro")

# Inserir itens no Treeview
item1 = treeview.insert("", "end", values=dados1)
item2 = treeview.insert("", "end", values=dados2)

# Expandir o primeiro item
treeview.item(item1, open=True)

# Empacotar o Treeview
treeview.pack()

# Iniciar o loop da janela
janela.mainloop()