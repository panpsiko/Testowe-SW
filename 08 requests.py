import requests
import requests

url_address = "http://api.nbp.pl/api/exchangerates/tables/A/"  # ?format=JSON

req_get = requests.get(url_address)

print(req_get)
# print(req_get.text)
dane = req_get.json()
print(dane)
print(type(dane))
print("-----------------------------------")
# for element in dane:
#     print(element, type(element))

slownik_waluty = dane[0]
print(type(slownik_waluty))
print("-----------------------------------")
print(slownik_waluty.keys())
kursy_walut = slownik_waluty["rates"]
print(type(kursy_walut))
print("-----------------------------------")
for waluta in kursy_walut:
    print(waluta, type(waluta))
    print(f"Dla {waluta['currency']} - kurs {waluta['mid']}")
    print("---")