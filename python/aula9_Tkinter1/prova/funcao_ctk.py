import customtkinter

def delete_message(widget):
    widget.grid_forget()

def conv_metro(valor, app):
    try:
        numero = float(valor)
        metro = customtkinter.CTkLabel(text=f"{numero/100} m", master=app, text_color="green")
        metro.grid(row=3,column=0)
        app.after(2000, lambda: delete_message(metro))
    except:
        metro = customtkinter.CTkLabel(text="Digite um número!", master=app, text_color="red")
        metro.grid(row=3,column=0)
        app.after(2000, lambda: delete_message(metro))


def conv_cent(valor, app):
    try:
        numero = float(valor)
        cent = customtkinter.CTkLabel(text=f"{numero*100} cm",master=app, text_color="green")
        cent.grid(row=3,column=1)
        app.after(2000, lambda: delete_message(cent))
    except:
        metro = customtkinter.CTkLabel(text="Digite um número!", master=app, text_color="red")
        metro.grid(row=3,column=1)
        app.after(2000, lambda: delete_message(metro))
