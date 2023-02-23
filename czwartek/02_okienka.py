# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element -----------------------------------------------------")],
    [sg.Text("Another text element"), sg.Text("ADAM")],
    [sg.Text("_______________________________________________________________________")],
    [sg.OK(), sg.Exit(), sg.Button("Przycisk"), sg.Button("GET WALUTA")],
]
window = sg.Window("Tutuł naszego okienka aplikacji", app_layout)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        print("Hard EXIT")
        break

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Event is: {event}, returned dict is: {values}")


# koniec programu
window.close()
print("End of application")