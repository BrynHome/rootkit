
import cryptography.fernet
from cryptography.fernet import Fernet


class encryption:
    def __init__(self, key):
        self.key = Fernet(key)

    def encrypt(self, data):
        return self.key.encrypt(data.encode('utf-8'))

    def decrypt(self, encrypted_data):
        try:
            d = self.key.decrypt(encrypted_data)
        except cryptography.fernet.InvalidToken:
            return b"Nope"
