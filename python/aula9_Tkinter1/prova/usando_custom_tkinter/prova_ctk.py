import customtkinter
from funcao_ctk import *

#Usando a biblioteca CustomTkinter

#Configuração da Tela
app = customtkinter.CTk()
app.title("Custom Tkinter")
app.configure(bg="black")

#Entrada Centímetro
cent_text = customtkinter.CTkLabel(master=app, text="Centímetros")
cent_text.grid(row=0, column=0)
cent_entry = customtkinter.CTkEntry(master=app)
cent_entry.grid(row=1, column=0)

#Saída Metro
button_m = customtkinter.CTkButton(master=app, text="Converter", command=lambda: conv_metro(cent_entry.get(), app))
button_m.grid(row=2,column=0)

#Entrada Metro
metr_text = customtkinter.CTkLabel(master=app, text="Metros")
metr_text.grid(row=0,column=1)
metr_entry = customtkinter.CTkEntry(master=app)
metr_entry.grid(row=1,column=1)

#Saída Centímetro
button_c = customtkinter.CTkButton(master=app, text="Converter", command=lambda: conv_cent(metr_entry.get(), app))
button_c.grid(row=2,column=1)


app.mainloop()