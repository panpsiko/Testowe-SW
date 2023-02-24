from secrets import token_hex
from sqlite3 import *
print(f"blah blah blah - {__name__} / To jest przetwarzane przy jakimkolwiek imporcie")

# https://sqlitebrowser.org/

def generate_token():
    new_token = token_hex(60)
    print(new_token)
    return new_token