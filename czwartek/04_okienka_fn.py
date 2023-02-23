# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg
import requests
import snakemd
import subprocess
import os  # https://docs.python.org/3/library/os.html
from secrets import token_urlsafe
from pathlib import Path

TEMP_DIR = "tmp"
NBP_URL = "https://api.nbp.pl/"

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
    try:
        nbp_test = requests.get(NBP_URL)
        status_nbp = nbp_test.status_code
    except Exception as e:
        sg.Popup(f"Error -> {e} | status_nbp ustawiam na -> -999", title="ERROR")
        status_nbp = -999

    if status_nbp == 200:
        sg.Popup(f"Łączność do {NBP_URL} - OK")
    elif status_nbp == -999:
        sg.Popup(f"Łączność do {NBP_URL} - sprawdź kabelek!!!!")
    else:
        sg.Popup(f"Łączność do {NBP_URL} - code: {status_nbp}")



# Start aplikacji
init_dir()

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