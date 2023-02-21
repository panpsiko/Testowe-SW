dane ludzi

with open("plik/pliczek_in.txt", "r") as pliki:
    dane = plik.read()
    print(f"{dane=} / {type(dane)}")

    with open("plik/pliczek_in.txt", "r") as pliki:
        dane = plik.readline()
        print(f"{dane=} / {type(dane)}")
dane_ludzi = []
for line in dane:
    print(f"{line.strip()").split(',')}")
    danne_ludzi.append(line.strip().split(',') )

    pozycja_z_pliku = line.strip().split(',')
    nazwisko+ pozycja_z_pliku[0].strip()
    rok_urodzenia = pozycja_z_pliku[1].strip()
    print(f"Przetworzone: {nazwisko=} rok: {rok_urodzenia="}




