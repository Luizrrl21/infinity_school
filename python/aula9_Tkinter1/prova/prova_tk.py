from tkinter import *
from funcao_tk import *

#Configuração da Tela
app = Tk()
app.title("Custom Tkinter")
app.configure(bg="black")

#Entrada Centímetro
cent_text = Label(master=app, text="Centímetros", bg="black", fg="white")
cent_text.grid(row=0, column=0)
cent_entry = Entry(master=app)
cent_entry.grid(row=1, column=0)

#Saída Metro
button_m = Button(master=app, text="Converter", command=lambda: conv_metro(cent_entry.get(), app))
button_m.grid(row=2,column=0)

#Entrada Metro
metr_text = Label(master=app, text="Metros", bg="black", fg="white")
metr_text.grid(row=0,column=1)
metr_entry = Entry(master=app)
metr_entry.grid(row=1,column=1)

#Saída Centímetro
button_c = Button(master=app, text="Converter", command=lambda: conv_cent(metr_entry.get(), app))
button_c.grid(row=2,column=1)


app.mainloop()