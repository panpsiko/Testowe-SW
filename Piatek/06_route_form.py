from flask import Flask, render_template, request

DATABASE = "funkcje_dodatkowe/user.db"

from funkcje_dodatkowe.baza_danych import generate_token, create_user_record, check_mail
from funkcje_dodatkowe.send_email_smarthost import mail_report
from datetime import datetime

app = Flask("moja_apka")


@app.route("/") # dekorator
def main_page():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def przechwyc_dane():
    pass

@app.route("/data")
def get_data():
    html = """
    <h2> Podaj nam dane </h2> <hr>
    Tu chcę Twój adres email: ...... <hr>
    """ + str(generate_token())
    return html

@app.route("/user/<value>")
def username(value):
    html = f"""
    <H1>Welcome new user</H1>
    Wysyłam ci maila na adres: {value}
    """
    new_token = generate_token()
    mail_body = f"treść naszego maila - {datetime.today()} - http://127.0.0.1:5000/clicked/{value}/{new_token}"
    if value.count("@") == 1:
        ret, ret_value = mail_report(value,"python-course@jurkiewicz.tech", mail_body)
        if ret == False:
            print(ret_value)
        if ret == True:
            retdb = create_user_record(DATABASE, value, new_token)
            print(f"Returned: {retdb}")
    return html

@app.route("/clicked/<mail>/<value>")
def username_click(mail, value):
    html = f"""
    <H1>A jednak, kliknięto ;-)</H1>
    Dla: {mail} - Wartość hash: {value} <hr>
    """
    sprawdzono = check_mail(DATABASE, mail, value)
    html += f"Czy się zgadza = {sprawdzono}"
    return html


app.run()