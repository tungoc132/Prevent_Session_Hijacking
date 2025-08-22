
from cryptography.fernet import Fernet
from Cryptodome.Cipher import AES
from Cryptodome import Random
import hashlib
import base64
from flask import session

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
        
    

    def GetKey(self, cipher_session):
            key = Session_Key_Dict[cipher_session]
            return key

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
        key = self.GetKey(session)
        cipher = AESCipher(key)
        return int(cipher.decrypt(session))



class ManageSession():
    def __init__(self):
        self.ES = EncryptionSession()

    def tCheckKey(self, session):
        if session in Session_Key_Dict:
            return True
        return False

    def CheckPlain(self, plain_session):
        plain_session = self.GetPlain(plain_session)
        if plain_session in Session_Value_Dict:
            return True

        return False

    def CheckSession(self, session):
        return session.get('id', None) is not None and self.tCheckKey(session.get('id'))




    def GetPlain(self, session):
        if (type(session) == str):
            return session
        elif (type(session) == bytes):
            return session.decode()
        return str(session)

    def GetNowCipher(self, session):
        session = self.GetPlain(session)
        if (session in Session_Value_Dict):
            return Session_Value_Dict[session]
        return None

    def GetNewCipher(self, session):
        session = self.GetPlain(session)
        return self.ES.encrypt_session(session)

    
    
    def GetDecipher (self, cipher_session):
        #if (type(cipher_session) != bytes):
         #   cipher_session = cipher_session.encode()
        try:
            key = Session_Key_Dict[cipher_session]
        except:
            return print("No key")
        
        return self.ES.decrypt_session(cipher_session)


    def DeleteSessionInDictWithPlain(self, session):
        session = self.GetPlain(session)
        if session in Session_Value_Dict:
            del Session_Key_Dict[Session_Value_Dict[session]]
            del Session_Value_Dict[session]

    

        
    


Session_Key_Dict = dict() # Dictionary for session_cipher : key
Session_Value_Dict = dict()# Dictionary for session_id : session_cipher















