# pentla iteracyjna + rózne sposoby f-string (od 3.8)

for value in range(5):
    print(f"Zmienna sterująca = {value}")
    print(f"Zmienna sterująca = {value=}")

print("--------------------------")       # nie róbcie tego na produkcji

for value in range(1, 5):
    print(f"Zmienna sterująca = {value=}")

    for value in range(1, 15, 3):
        print(f"Zmienna sterująca = {value=}")