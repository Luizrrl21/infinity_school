from tkinter import *

janela = Tk()
janela.title("Aula 1 Tkinter")
# janela.geometry("400x400")
# janela.attributes('-fullscreen', True)
janela.state('zoomed')
janela.configure(bg="black")

def media():
    n1 = int(nota1_entry.get())
    n2 = int(nota2_entry.get())
    md = (n1+n2)/2
    if md >= 7:
        message = Label(text=f"Media: {md}", bg="black", fg="green")
        message.pack()
        # janela.after(1000, lambda: delete_message(message))

nota1_title = Label(text="1º Nota:", bg="black", fg="white")
nota1_title.pack()
nota1_entry = Entry()
nota1_entry.pack()

nota2_title = Label(text="2º Nota:", bg="black", fg="white")
nota2_title.pack()
nota2_entry = Entry()
nota2_entry.pack()

botao = Button(janela, text="Enviar", command=media)
botao.pack()

janela.mainloop()