import snakemd
from secrets import token_urlsafe # https://docs.python.org/3/library/secrets.html

plik = f"pliki/{token_urlsafe(8)}"
nowy_dokument = snakemd.new_doc(plik)


nowy_dokument.output_page()

