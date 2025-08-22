
from cryptography.fernet import Fernet
from Cryptodome.Cipher import AES
from Cryptodome import Random
import hashlib
import base64

class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode()

    def _pad(self, s):       
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    
    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

class EncryptionSession(object):
    def __init__(self):
        pass
        

    def encrypt_session(self, plain):
        if (plain in Session_Value_Dict):
            del Session_Key_Dict[Session_Value_Dict[plain]]
            
            
        key = Fernet.generate_key()
        cipher_session = AESCipher(key)  
        x = cipher_session.encrypt(plain)
        Session_Key_Dict[x] = key  
        Session_Value_Dict[plain] = x    
        return x

    def decrypt_session(self, session):
        cipher_session = AESCipher(Session_Key_Dict[session])
        return cipher_session.decrypt(session)




Session_Key_Dict = dict()
Session_Value_Dict = dict()
EncryptionS = EncryptionSession()











