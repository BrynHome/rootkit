from cryptography.fernet import Fernet


class encryption:
    def __init__(self, key):
        self.key = Fernet(key)

    def encrypt(self, data):
        return self.key.encrypt(bytes(data, 'utf-8'))

    def decrypt(self, encrypted_data):
        return self.key.decrypt(encrypted_data)
