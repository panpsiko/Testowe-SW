from flask import Flask

from funkcje_dodatkowe.baza_danych import generate_token



app = Flask("moja_apka")

@app.route("/") # dekorator
def main_page():
    return "<H1> Welcome</H1>"

@app.route("/data")
def get_data():
    html = """
    <h2> Podaj nam dane </h2> <hr>
    Tu chcę Twój adres email: ...... <hr>
    """ + str(generate_token())
    return html

app.run()