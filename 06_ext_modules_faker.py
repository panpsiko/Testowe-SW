from faker import Faker

from faker import Faker

ludzik = Faker("pl-PL")

for _ in range(10):
    print(ludzik.name(), ludzik.address(), ludzik.iban(), ludzik.credit_card_full())