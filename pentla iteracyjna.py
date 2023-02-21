# pentla iteracyjna + iterables

imie = "Adam"
wiek = 50
lista_2 = [3, 14, 54, 55]
lista = [3, 54, 3, wiek, 5, lista_2, 8, imie, 9]

for element in lista:
    print(f"Wartość {element=} ma typ {type(element)}")
    print(f"Litera to {chr(element)}")
    if isinstance(element, int):
        print(f"Litera to {chr(element)}")
    elif isinstance(element, list):
        print(f"Teraz lista wewnętrzna - {element}")
        for inny in element:
            print(f"Litera wewnetrzna to {chr(inny)}")
            elif isinstance(element, str):
            print(f"Teraz lista wewnętrzna - {element}")
            for inny in element:
                print(f"Litera wewnetrzna ma kod {ord(inny)}")
    else:
        print("Sorry")

