# pentla iteracyjna + literki
# od a do z

#wersja 1 - litery
alphabet = 'abcdefghijklmnoprstuwxyz'

for letter in alphabet:
    # print(f"Letter is {letter}")
    # a / b / c/d ..........
    # print(letter, end=" /")
    print(f"Letter is {letter}", end="/")

for letter in enumerate(alphabet):
    print(f"Letter is {letter}")

    print("----------------------")
    for position, letter in enumerate(alphabet):
        print(f"Letter is {letter}, {position=}")
        if position == 7:
            print("Siódemka!!!")


