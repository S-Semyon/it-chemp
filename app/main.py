from flet import app

from app.pages.index import create_counter_page


def main(page):
    create_counter_page(page)


app(target=main, port=8080)
