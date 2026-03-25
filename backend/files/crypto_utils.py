from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def load_public_key():
    with open("keys/public.pem", "rb") as f:
        return serialization.load_pem_public_key(f.read())


def load_private_key():
    with open("keys/private.pem", "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def encrypt_key_with_rsa(aes_key: bytes) -> bytes:
    public_key = load_public_key()
    return public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def decrypt_key_with_rsa(encrypted_key: bytes) -> bytes:
    private_key = load_private_key()
    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


