from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

#AES Encryption+ Decryption

def encrypt(data:bytes, key: bytes):
    iv = os.urandom(12)
    aesgcm = AESGCM(key)
    encrypted = aesgcm.encrypt(iv, data, None)
    
    ciphertext = encrypted[:-16]
    tag = encrypted[-16:]

    return ciphertext, iv, tag


def decrypt(ciphertext:bytes, key:bytes, iv:bytes, tag:bytes):
    aesgcm = AESGCM(key)
    encrypted = ciphertext + tag

    decrypted = aesgcm.decrypt(iv, encrypted, None)
    return decrypted
    