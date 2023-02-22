

imie = "Adam"
wiek = 49
lista_2 = [3.14, 55, 54]
lista = [63, 54, 93, wiek, 45, lista_2, 8, imie, 9]

for element in lista:
    print(f"Wartość {element=} ma typ {type(element)}")
    if isinstance(element, int):
        print(f"Litera to {chr(element)}")
    elif isinstance(element, list):
        print(f"Teraz lista wewnętrzna - {element}")
        for inny in element:
            print(f"Litera wewnętrzna to {chr(inny)}")
    elif isinstance(element, str):
        print(f"Teraz string wewnętrzna - {element}")
        for inny in element:
            print(f"Litera wewnętrzna ma kod {ord(inny)}")

    else:
        print("Sorry")