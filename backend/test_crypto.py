import os
from files.crypto_utils import encrypt_key_with_rsa, decrypt_key_with_rsa

# 1. Générer une clé AES aléatoire
original_key = os.urandom(32)

print("Original key:", original_key)

# 2. Chiffrer avec RSA
encrypted_key = encrypt_key_with_rsa(original_key)
print("Encrypted key:", encrypted_key)

# 3. Déchiffrer avec RSA
decrypted_key = decrypt_key_with_rsa(encrypted_key)
print("Decrypted key:", decrypted_key)

# 4. Vérifier
print("Match:", original_key == decrypted_key)