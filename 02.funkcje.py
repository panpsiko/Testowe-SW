# petla iteracyjna + iterables

def info_znak(liczba):
    # f"Litera to {chr(element)}"
    znak = chr(liczba)
    co_zwracam = f"Litera to {znak}"
    return co_zwracam

imie = "Adam"
wiek = 49
lista_2 = [3,14, 55, 54]
lista = [63, 54, 93, wiek, 45, lista_2, 8, imie, 9]

for element in lista:
    print(f"Wartość {element=} ma typ {type(element)}")
    if isinstance(element, int):
        print(info_znak(element))
    elif isinstance(element, list):
        print(f"Teraz lista wewnętrzna - {element}")
        for inny in element:
            print(info_znak(inny))
    elif isinstance(element, str):
        print(f"Teraz string wewnętrzna - {element}")
        for inny in element:
            print(f"Litera wewnętrzna ma kod {ord(inny)}")

    else:
        print("Sorry")
