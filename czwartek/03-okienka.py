# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text(" --[Generowanie DOCX z wykresem walut------------------------------")],
    [sg.Text("Podaj kod Waluty (np. CHF)"), sg.Input("")],
    [sg.Text("_______________________________________________________________________")],
    [sg.Text("Ile dni wstecz wykres (max. 30)?"), sg.Input("")],
    [sg.Button("GENERUJ"),sg.Button("TEST INTERNETU"), sg.Button("KONIEC") ],
]
window = sg.Window("Tutuł naszego okienka aplikacji", app_layout)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "KONIEC":
        print("Hard EXIT")
        break

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Event is: {event}, returned dict is: {values}")


# koniec programu
window.close()
print("End of application")