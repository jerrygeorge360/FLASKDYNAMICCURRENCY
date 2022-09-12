import requests
import os


def ninja_currency(base_currency='', location_currency='', amount=''):
    url = f'https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency'
    querystring = {"have": base_currency, "want": location_currency, "amount": amount}
    headers = {
        "X-RapidAPI-Key": os.environ.get('api_key_ninja'),
        "X-RapidAPI-Host": os.environ.get('api_host_ninja')
    }
    response = requests.request("GET", url=url, headers=headers, params=querystring).json()
    new_currency = response.get('new_amount')
    return new_currency


def free_currency(base_currency='', location_currency=''):
    url = "https://freecurrencyapi-free-currency-data.p.rapidapi.com/rates"
    headers = {
        "X-RapidAPI-Key": os.environ.get('api_free_key'),
        "X-RapidAPI-Host": os.environ.get('api_free_host')
    }
    response = requests.request("GET", url, headers=headers)

    print(response.text)


def currency_net(base_currency='', location_currency='', amount=''):
    url = "https://currencyapi-net.p.rapidapi.com/convert"

    querystring = {"from": base_currency, "to": location_currency, "amount": amount, "output": "JSON"}
    headers = {
        "X-RapidAPI-Key": os.environ.get('currency_net_key'),
        "X-RapidAPI-Host": os.environ.get('currency_net_host')
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# base currency must be in dollars.
def exchange_rate(base_currency='USD', location_currency=''):
    url = f"https://exchangerate-api.p.rapidapi.com/rapid/latest/f'{base_currency}'"

    headers = {
        "X-RapidAPI-Key": os.environ.get('exchange_rate_key'),
        "X-RapidAPI-Host": os.environ.get('exchange_rate_host')
    }
    response = requests.request("GET", url, headers=headers)

    print(response.text)
