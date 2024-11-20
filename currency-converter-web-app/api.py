import requests

def get_url(url: str):
    response = requests.get(url)

    return response.status_code, response.text
