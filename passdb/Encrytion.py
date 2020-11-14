from cryptography.fernet import Fernet
from KEY import KEY


class Encryption:
    def encoder(data, password):
        encrypted = Fernet(KEY.CheckKey(password)).encrypt(data)
        return encrypted

    def decoder(data, password):
        decoded = Fernet(KEY.CheckKey(password)).decrypt(data).decode()
        return decoded
