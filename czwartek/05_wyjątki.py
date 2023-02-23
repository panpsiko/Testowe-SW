try:
    # sprawdzenie
    aa = "a" + q
except NameError:
    print("brak zmiennej")
except KeyError:
    print("zły klucz dla słownika")
except Exception as e:
    print(e)