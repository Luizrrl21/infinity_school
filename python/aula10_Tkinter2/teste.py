import tkinter as tk
from tkinter import messagebox

def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) > 6 and "@" in email:
        messagebox.showinfo("Login Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro no Login", "Verifique seu e-mail e senha.")

# Criar janela
janela = tk.Tk()
janela.title("Interface de Login")

# Labels e Entradas
label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_email = tk.Entry(janela)
entry_email.grid(row=0, column=1, padx=10, pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_senha = tk.Entry(janela, show="*")  # Mostra asteriscos para a senha
entry_senha.grid(row=1, column=1, padx=10, pady=5)

# Botão de Login
botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar o loop da janela
janela.mainloop()
