import requests


def get(url, params=None):
    response = requests.get(url, params=params)
    return response.json()
