from tkinter import *
import time

janela = Tk()
janela.title("Aula 1 Tkinter")
# janela.geometry("400x400")
# janela.attributes('-fullscreen', True)
janela.state('zoomed')
janela.configure(bg="black")

def delete_message(widget):
    widget.pack_forget()

def mostrar_idade():
    if int(idade.get()) >= 18:
        message = Label(text="Maior de idade!", bg="black", fg="green")
        message.pack()
        janela.after(1000, lambda: delete_message(message))

    elif int(idade.get()) < 18:
        message = Label(text="Menor de idade!", bg="black", fg="red")
        message.pack()
        janela.after(1000, lambda: delete_message(message))

    else:
        print("Type error")

idade = Label(text="Digite sua idade:", bg="black", fg="white")
idade.pack()

idade = Entry()
idade.pack()

botao = Button(janela, text="Enviar", command=mostrar_idade)
botao.pack()

janela.mainloop()
