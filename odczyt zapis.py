with open("plik/pliczek_in.txt", "r") as pliki:
    dane = plik.read()
    print(f"{dane=} / {type(dane)}")

    with open("plik/pliczek_in.txt", "r") as pliki:
        dane = plik.readline()
        print(f"{dane=} / {type(dane)}")

for line in dane:
    print(f"{line.strip()}")