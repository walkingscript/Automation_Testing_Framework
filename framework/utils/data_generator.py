import random
import secrets
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits


class DataGen:

    CYRILLIC_LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    DOMAINS = ('yandex', 'google', 'mail')

    @staticmethod
    def generate_string(length=15):
        symbols = ascii_letters + digits
        ls = random.choices(symbols, k=length)
        return ''.join(ls)

    @classmethod
    def generate_password(
        cls, length=10, lowercase=True, uppercase=True, digits_=True,
        cyrillic=False, salt=''
    ):
        symbols = ''
        password = ''
        if lowercase:
            symbols += ascii_lowercase
            password += secrets.choice(ascii_lowercase)
        if uppercase:
            symbols += ascii_uppercase
            password += secrets.choice(ascii_uppercase)
        if digits_:
            symbols += digits
            password += secrets.choice(digits)
        if cyrillic:
            cyrillic_all = cls.CYRILLIC_LOWER + cls.CYRILLIC_LOWER.upper()
            symbols += cyrillic_all
            password += secrets.choice(cyrillic_all)
        if salt:
            # required only letters
            salt_letters = ''.join([char for char in salt if char.isalpha()])
            password += secrets.choice(salt_letters)
        for _ in range(length-len(password)):
            password += secrets.choice(symbols)
        password_chars = list(password)
        random.shuffle(password_chars)
        return ''.join(password_chars)

    @classmethod
    def generate_email_domain(cls):
        return secrets.choice(cls.DOMAINS)
