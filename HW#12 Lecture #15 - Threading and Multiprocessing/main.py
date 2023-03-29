import threading
import requests
import json


def get_nbu_currency():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def get_privatbank_currency():
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def compare_currencies():
    nbu_data = get_nbu_currency()
    privatbank_data = get_privatbank_currency()

    nbu_usd = float(next(item for item in nbu_data if item["cc"] == "USD")["rate"])
    pb_usd = float(next(item for item in privatbank_data if item["ccy"] == "USD")["buy"])

    nbu_eur = float(next(item for item in nbu_data if item["cc"] == "EUR")["rate"])
    pb_eur = float(next(item for item in privatbank_data if item["ccy"] == "EUR")["buy"])

    if nbu_usd < pb_usd:
        print("USD exchange rate is better at NBU")
    else:
        print("USD exchange rate is better at Privatbank")

    if nbu_eur < pb_eur:
        print("EUR exchange rate is better at NBU")
    else:
        print("EUR exchange rate is better at Privatbank")


def calculate_exchange(currency, amount):
    nbu_data = get_nbu_currency()
    privatbank_data = get_privatbank_currency()

    if currency == "USD":
        nbu_rate = float(next(item for item in nbu_data if item["cc"] == "USD")["rate"])
        pb_rate = float(next(item for item in privatbank_data if item["ccy"] == "USD")["buy"])
    elif currency == "EUR":
        nbu_rate = float(next(item for item in nbu_data if item["cc"] == "EUR")["rate"])
        pb_rate = float(next(item for item in privatbank_data if item["ccy"] == "EUR")["buy"])
    else:
        print("Invalid currency")
        return

    nbu_exchange = amount * nbu_rate
    pb_exchange = amount * pb_rate

    if nbu_exchange > pb_exchange:
        print(f"Exchange at NBU is more profitable, you will get {nbu_exchange} UAH")
    else:
        print(f"Exchange at Privatbank is more profitable, you will get {pb_exchange} UAH")


if __name__ == "__main__":
    nbu_thread = threading.Thread(target=get_nbu_currency)
    pb_thread = threading.Thread(target=get_privatbank_currency)
    compare_thread = threading.Thread(target=compare_currencies)

    nbu_thread.start()
    pb_thread.start()
    compare_thread.start()

    nbu_thread.join()
    pb_thread.join()
    compare_thread.join()

    calculate_exchange("USD", 100)
    calculate_exchange("EUR", 100)
