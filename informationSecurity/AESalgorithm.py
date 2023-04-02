import base64
import hashlib
from Crypto.Cipher import AES

BS = 16
pad = (lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode())
unpad = (lambda s: s[:-ord(s[len(s)-1:])])

class AESCipher(object):
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
    
    def encrypt(self, message):
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, self.__iv().encode('utf8'))
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')
    
    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.__iv().encode('utf8'))
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')
    
    def __iv(self):
        return chr(0) * 16

def menu1(data):
    encrypt = aes.encrypt(data)
    print("암호화:", encrypt)

def menu2(data):
    decrypt = aes.decrypt(data)
    print("복호화:", decrypt)

key = "201700980"

aes = AESCipher(key)

print("1. 암호화")
print("2. 복호화")
menu = input("메뉴를 선택하세요 ")
data = input("문장 : ")

if menu == "1":
    menu1(data)
else:
    menu2(data)

