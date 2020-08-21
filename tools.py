from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex



class Pycrypto():
    """
    密码加密解密
    key必须大于16字符
    加密内容为16的倍数
    """
    def __init__(self, key, text):
        self.key = key
        self.text = text
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.key.encode(), self.mode)

    def encrypt(self):
        encryption_info = b2a_hex(self.cryptor.encrypt(self.text.encode()))
        return encryption_info

    def decrypt(self):
        decryption_info = self.cryptor.decrypt(a2b_hex(self.text)).decode()
        return decryption_info





