colors = ["red", "grean"]

# teraz user podaje własne kolory
ile = int(input("Ile chcesz dodać kolorów: "))
for new in range(ile):
    new_color = input("Jaki chcesz kolor? ")

for color in colors:
    print(f"{color=}")
