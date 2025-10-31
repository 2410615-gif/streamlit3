import requests

url = "https://api.exchangerate.host/latest?base=USD"
rates = requests.get(url).json()["rates"]

amount = float(input("USD 금액: "))
target = input("변환할 통화 (KRW, JPY, EUR 등): ").upper()
print(f"{amount} USD = {amount * rates[target]:.2f} {target}")
