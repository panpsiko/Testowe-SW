import csv
from faker import Faker

ludzik = Faker("pl-PL")

with open("ludzie.csv", "w", newline='') as plik_csv:
    csv_writer = csv.writer(plik_csv, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    for _ in range(10):
        csv_writer.writerow([ludzik.name(), ludzik.company(), ludzik.company_vat(), ludzik.local_regon()])

