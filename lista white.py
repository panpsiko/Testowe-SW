colors = [ ]

# teraz user podaje własne kolory - pętla nieskończoności
while True:

    new_color = (input("Ile chcesz dodać kolorów: "))

    if new_color == "KONIEC":
        break
    colors.append(new_color)

print(colors)

for color in colors:
    print(f"{color=}")
