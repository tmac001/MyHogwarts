# @Time : 2020-04-13 11:50
import requests


def test_requests():
    r = requests.get("https://home.testing-studio.com/c/opensource/17.json")
    print(r.json())

    print(type(r.json()))
