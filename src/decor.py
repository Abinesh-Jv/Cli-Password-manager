from src import encryp

def encrypt(f):
    def wrapper(*args,**kwargs):
        rv = f(*args,**kwargs)
        en_rv = encryp.encrypt_message(rv)
        return en_rv,rv
    return wrapper

def decrypt(f):
    def wrapper(*args,**kwargs):
        rv = f(*args,**kwargs)
        en_rv = encryp.decrypt_message(rv)
        return en_rv,rv
    return wrapper


