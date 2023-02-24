import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email_imap(username, password, recipient, subject, body, attachment=None):
    # Create a new SMTP object and connect to the Gmail SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
    smtp_conn.ehlo()
    smtp_conn.starttls()
    smtp_conn.ehlo()
    smtp_conn.login(username, password)

    # Create a new MIME message object and fill in the details
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # Attach a file if specified
    if attachment is not None:
        with open(attachment, 'rb') as f:
            part = MIMEApplication(f.read(), Name=attachment)
            part['Content-Disposition'] = f'attachment; filename="{attachment}"'
            msg.attach(part)

    # Convert the message to a string and send it via SMTP
    smtp_conn.sendmail(username, recipient, msg.as_string())

    # Disconnect from the SMTP server
    smtp_conn.quit()

    # Connect to the Gmail IMAP server and mark the email as read
    imap_server = 'imap.gmail.com'
    imap_port = 993
    imap_conn = imaplib.IMAP4_SSL(imap_server, imap_port)
    imap_conn.login(username, password)
    imap_conn.select('INBOX')
    imap_conn.search(None, 'UNSEEN')
    _, data = imap_conn.fetch(data[0].split()[0], '(RFC822)')
    imap_conn.store(data[0].split()[0], '+FLAGS', '\\Seen')
    imap_conn.close()
    imap_conn.logout()
