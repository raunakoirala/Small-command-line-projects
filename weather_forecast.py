import requests
import json

api_key = "f32bb36331a4483817114cac4be9f60"
from_currency = input("Enter the currency you want to convert from: ")
to_currency = input("Enter the currency you want to convert to: ")
amount = input("Enter the amount: ")

url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    rate = data["rates"][to_currency] / data["rates"][from_currency]
    converted_amount = rate * float(amount)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
else:
    print