from flask import Flask

app = Flask("moja_apka")

@app.route("/") # dekorator
def main_page():
    return "<H1> Welcome</H1>"

@app.route("/data")
def get_data():
    html = """
    <h2> Podaj nam dane </h2> <hr>
    Tu chcę Twój adres email: ...... <hr>
    """
    return html

app.run()