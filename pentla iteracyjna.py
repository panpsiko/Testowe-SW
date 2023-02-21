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
    else:
        print("Sorry")
