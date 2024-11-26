from flet import app

from app.pages.login import create_login_page


def main(page):
    create_login_page(page)


app(target=main, port=8080)
