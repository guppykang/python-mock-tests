import requests


def ping_server():
    response = requests.get('http://127.0.0.1:5000/')
    if response.ok:
        return response
    else:
        return None
