from tkinter import *
from tkinter import ttk
# from main import *

#Configurações Gerais
app = Tk()
app.title("Gerenciamento Biblioteca")
app.geometry("360x500")
app.configure(bg="gray")

#Adicionando Navegação
tab_control = ttk.Notebook(app)

#Tab 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Livros")
tab_control.pack(expand=1, fill="both")

#Título
titulo_name = Label(master=tab1,text="Titulo").grid(row=1, column=0)
titulo_entry = Entry(master=tab1).grid(row=1, column=1)
#Autor
autor_name = Label(master=tab1, text="Autor").grid(row=2, column=0)
autor_entry = Entry(master=tab1).grid(row=2, column=1)
#ID
id_name = Label(master=tab1, text="ID").grid(row=3, column=0)
id_entry = Entry(master=tab1).grid(row=3, column=1)

#Ação
def get_value():
   e_text=titulo_entry.get()
   print(e_text)



# #Status
# status = Checkbutton(master=tab1, text="Disponível").grid(row=4, column=1)
Label(master=tab1,text="").grid(row=4)

botao = Button(master=tab1, text="Adicionar Livro", width=24, command=get_value).grid(row=5, column=0)
botao = Button(master=tab1, text="Procurar Livros", width=24).grid(row=5, column=1)

































#Tab 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Membros")
tab_control.pack(expand=2, fill="both")

app.mainloop()