import requests

from .types import User

ADDR = "127.0.0.1:8000"
SECRET_KEY = "AAABBB"


def check_token(token: str) -> User:
    response = requests.post(
        ADDR + "/socket/check_token", json={"access": SECRET_KEY, "token": token}
    )
    data = response.json()
    return data["user"]


def send_notify(username: str) -> User:
    requests.post(
        ADDR + "/socket/check_token", json={"access": SECRET_KEY, "username": username}
    )
