dane = [{'table': 'A', 'no': '037/A/NBP/2023', 'effectiveDate': '2023-02-22', 'rates':
    [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.1292}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.4687}, {'currency': 'dolar australijski', 'code': 'AUD', 'mid': 3.0482}]}]

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