import flet as ft

def main(page: ft.Page):
    page.title = "Greeting App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 500

    name_input = ft.TextField(
        label="Your name",
        hint_text="Type your name here",
        width=300,
        autofocus=True
    )

    result_text = ft.Text(
        value="",
        size=22,
        weight=ft.FontWeight.W_600
    )

    def on_greet_tapped(e):
        entered = name_input.value.strip()
        if entered:
            result_text.value = f"Hello, {entered}!"
        else:
            result_text.value = "Please enter a name first."
        page.update()

    greet_button = ft.ElevatedButton(
        text="Greet Me",
        width=300,
        on_click=on_greet_tapped
    )

    layout = ft.Column(
        controls=[
            name_input,
            greet_button,
            ft.Divider(height=20, color="transparent"),
            result_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)