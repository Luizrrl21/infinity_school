import tkinter as tk

def logar():
    email = entry_email.get()
    senha = entry_senha.get()

    def apagar():
        erro.pack_forget()

    if len(senha) > 6 and "@" in email:
        certo = tk.Label(text="Login realizado com sucesso!", fg="green")
        certo.pack()
        label_email.pack_forget()
        entry_email.pack_forget()
        label_senha.pack_forget()
        entry_senha.pack_forget()
        botao_login.pack_forget()
    else:
        erro = tk.Label(text="Verifique seu e-mail e senha.", fg="red")
        erro.pack()
        erro.after(2000, apagar)

app = tk.Tk()
app.geometry("300x300")
app.title("Login Infinity")

label_email = tk.Label(app, text="E-mail:")
entry_email = tk.Entry(app)
label_senha = tk.Label(app, text="Senha:")
entry_senha = tk.Entry(app, show="*")
botao_login = tk.Button(app, text="Login", command=logar)

label_email.pack()
entry_email.pack()
label_senha.pack()
entry_senha.pack()
botao_login.pack()

app.mainloop()
