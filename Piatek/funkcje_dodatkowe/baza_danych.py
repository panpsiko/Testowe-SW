from secrets import token_hex
print(f"blah blah blah - {__name__} / To jest przetwarzane przy jakimkolwiek imporcie")

def generate_token():
    new_token = token_hex(60)
    print(new_token)
    return new_token