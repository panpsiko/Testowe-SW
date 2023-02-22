def przelicz_walute(kod, wartosc, kurs):
    wart_zwracana = round(wartosc * kurs, 2)
    napis = f"Dla waluty {kod} - po kursie {kurs}, ilość {wartosc} to {wart_zwracana}"
    return napis

print(przelicz_walute("chf", 13.4, 4.8634))