from tkinter import *

def delete_message(widget):
    widget.grid_forget()

def conv_metro(valor, app):
    try:
        numero = float(valor)
        metro = Label(text=f"{numero/100} m",master=app, bg="black", fg="green")
        metro.grid(row=3,column=0)
        app.after(2000, lambda: delete_message(metro))
    except:
        metro = Label(text="Digite um número",master=app, bg="black", fg="red")
        metro.grid(row=3,column=0)
        app.after(2000, lambda: delete_message(metro))

def conv_cent(valor, app):
    try:
        numero = float(valor)
        cent = Label(text=f"{numero*100} cm",master=app, bg="black", fg="green")
        cent.grid(row=3,column=1)
        app.after(2000, lambda: delete_message(cent))
    except:
        metro = Label(text="Digite um número",master=app, bg="black", fg="red")
        metro.grid(row=3,column=0)
        app.after(2000, lambda: delete_message(metro))