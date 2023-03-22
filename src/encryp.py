from cryptography.fernet import Fernet

def load_key():
    return open("utils\\encryption_key.jv", "rb").read()

def encrypt_message(message):

    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    
    return decrypted_message.decode()