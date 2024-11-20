from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    url = f'{BASE_URL}/currencies'
    status_code, text = get_url(url)

    if status_code != 200:
        return None
    
    try:
        return list(json.loads(text).keys())
    except Exception:
        return None
    

def get_latest_rates(from_currency, to_currency, amount):
    url = f'{BASE_URL}/latest?amount={amount}&from={from_currency}&to={to_currency}'

    status_code, text = get_url(url)

    if status_code != 200:
        return None, None
    
    try:
        data: dict = json.loads(text)
        return data.get("date"), data.get("rates").get(to_currency) / amount
    except Exception:
        return None
    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    url = f'{BASE_URL}/{from_date}?amount={amount}&from={from_currency}&to={to_currency}'

    status_code, text = get_url(url)

    if status_code != 200:
        return None
    
    try:
        data: dict = json.loads(text)
        return data.get("rates").get(to_currency) / amount
    except Exception:
        return None
    
    

