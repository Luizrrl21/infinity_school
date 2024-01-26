import tkinter as tk
from tkinter import ttk

def redimensionar(event):
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    status_var.set(f"Largura: {largura} | Altura: {altura}")

# Criar janela
janela = tk.Tk()
janela.title("Exemplo de Sizegrip")

# Adicionar widgets à janela
frame = ttk.Frame(janela)
frame.pack(expand=True, fill="both")

# Adicionar Sizegrip
sizegrip = ttk.Sizegrip(frame)
sizegrip.grid(row=1, column=1, sticky="se")

# Adicionar uma label para mostrar as dimensões da janela
status_var = tk.StringVar()
status_label = ttk.Label(frame, textvariable=status_var)
status_label.grid(row=0, column=0, padx=10, pady=10)

# Vincular evento de redimensionamento à função
janela.bind("<Configure>", redimensionar)

# Iniciar o loop da janela
janela.mainloop()