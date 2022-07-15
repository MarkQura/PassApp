import base64
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KEY:
    def password(passlen=16):
        s = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&/()=?}][{@,;.:-_+*'
        passw = "".join(random.sample(s, passlen))
        return passw

    def CheckKey(password_provided):
        password_provided
        password = password_provided.encode()
        salt = b"|\x87\x00.WS\xc3\xa4\x01\xbc\x9e\xbe\x1b\xd8\xb8\xc7"

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend(),
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
