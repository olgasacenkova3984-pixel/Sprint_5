from random import randint

class Credentials:
    name = "Ольга"
    email = "shachenkova_49_111@yandex.ru"
    password = "pasw123"

class RandomUser:
    name = f"random{randint(0, 999)}Name"
    email = f"random{randint(000, 999)}mail@gmail.com"
    password = f"pas{randint(000, 999)}"

class InvalidRandomUser:
    name = f"random{randint(0, 999)}Name"
    email = f"random{randint(000, 999)}mail@gmail.com"
    invalid_password = f"{randint(000, 999)}"