# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg
import requests
import snakemd
import subprocess
import os
from secrets import token_urlsafe
from pathlib import Path

TEMP_DIR = "tmp"

def init_dir():
    if not Path(TEMP_DIR).exists():
        os.mkdir(TEMP_DIR)


def generuj_dokument():
    plik = f"{TEMP_DIR}/{token_urlsafe(8)}"
    nowy_dokument = snakemd.new_doc(plik)
    try:
        nowy_dokument.output_page()
    except Exception as e:
        sg.Popup(e, title="ERROR")

def test_internetu():
    pass

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

    if event == "GENERUJ":
        generuj_dokument()

    if event == "TEST INTERNETU":
        test_internetu()

    # sprawdzamy wartości zwracane przez okno
    sg.popup(f"Event is: {event}, returned dict is: {values}")


# koniec programu
window.close()
print("End of application")