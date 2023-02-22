def przelicz_walute(kod, wartosc, kurs):
    """
    Tu jakiś opis, np. nasza super funkcja
    :param kod: znakowy symbol waluty, np. CHF
    :param wartosc: ile chcemy waluty: float
    :param kurs: kurs waluty z dnia -> float, np. 4.8166
    :return: ładnie sformatowany string informacyjny
    """
    wart_zwracana = round(wartosc * kurs, 2)
    napis = f"Dla waluty {kod} - po kursie {kurs}, ilość {wartosc} to {wart_zwracana}"
    return napis

print(przelicz_walute("chf", 13.4, 4.8634))
przelicz_walute()
