from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from key import write_to_file
import base64

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    write_to_file(private_key, "private_key.pem")
    write_to_file(public_key, "public_key.pem")
    return private_key, public_key

def encrypt(message, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher.encrypt(message.encode())
    encrypted_message = base64.b64encode(encrypted_message).decode()
    return encrypted_message

def decrypt(encrypted_message, private_key):
    private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key)
    encrypted_message = base64.b64decode(encrypted_message)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message
