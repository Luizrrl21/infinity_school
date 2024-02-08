import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora IMC"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    peso = ft.TextField(text_align=ft.TextAlign.RIGHT, width=100)
    altura = ft.TextField(text_align=ft.TextAlign.RIGHT, width=100)

    def calculo(e):
        imc = round(float(peso.value)/(float(altura.value)**2),1)
        page.add(ft.Text(imc))
        page.update()

    page.add(
        ft.Row(
            [
                ft.Text("Peso"),
                peso,
                ft.Text("Altura"),
                altura,
                ft.ElevatedButton(text="Calcular", on_click=calculo),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)