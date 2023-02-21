klasa = [
    ("Sławek Wiciak", 1978),
    ("Marek Jurek", 1767),
    ("Tadeusz Krawczyk", 1948),
]

for preson in klasa:
    print(f"{preson=}")

for person_2, year in klasa:
    print(f"{person_2=} ->> {year}")


# zapis do pliku

with open("pliczek.txt", "w") as plik:
    for person in klasa:
    plik.write(str(person) + chr(10))

