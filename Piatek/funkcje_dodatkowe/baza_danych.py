from secrets import token_hex
from sqlite3 import *
import os
print(f"blah blah blah - {__name__} / To jest przetwarzane przy jakimkolwiek imporcie")


# https://sqlitebrowser.org/

def generate_token():
    new_token = token_hex(60)
    print(new_token)
    return new_token

def create_user_record(db, user, token):
    field_1 = "mail"
    field_2 = "token"
    new_values = (user, token)
    if os.path.exists(db):
        connection = connect(db)
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO userdata ({field_1},{field_2}) VALUES (?,?)', new_values)
        connection.commit()
        connection.close()
        return True
    else:
        return False


