import smtplib, ssl
from email.mime.text import MIMEText

# dane testowe Adama
_mail_from = "python-course@jurkiewicz.tech"
_login =  "python-course@jurkiewicz.tech"
_passwd = "504d8751dfe712b7db89b76075"

def mail_report(mail_to: str, mail_from: str, data: str) -> bool:  # type annotation
    ip = "jurkiewicz.tech"
    port = 465  # For SSL
    login = _login
    password = _passwd
    # password = "zle_haslo"
    ####

    text_type = 'plain'  # or 'html'
    msg = MIMEText(data, text_type, 'utf-8')
    msg['Subject'] = "Temat wiadomości"
    msg['From'] = mail_from
    #
    msg['To'] = mail_to

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(ip, port, context=context) as server:
            server.login(login, password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        return (True, "Test mail SUCCESS")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    print(f"to jest tylko uruchomienie testowe: {__name__}")
    mail_ok, report = mail_report("adam@jurkiewicz.tech", _mail_from, "Treść INNA")
    if mail_ok:
        print(report)
    else:
        print(f"Test mail failed - {report}")
else:
    print(f"Importujemy moduł: {__name__}")