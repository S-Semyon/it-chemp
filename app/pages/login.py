import flet as ft


def create_login_page(page: ft.Page):
    page.title = "SecViChat"
    page.vertical_alignment = "center"
    page.horizontal_alignment= "center"

    def login_click(e):
        print(123)

    page.add(
        ft.Column(
            [
                ft.TextField(text_align="left", width=500, label="Имя пользователя"),
                ft.TextField(text_align="left", width=500, password=True, can_reveal_password=True, label="Пароль"),
                ft.FilledButton(text="Войти", on_click=login_click),
            ],
            alignment="center", horizontal_alignment="center",

        )
    )
