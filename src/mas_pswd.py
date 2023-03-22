from src import encryp
import os

def check(pwd):
    with open("utils\\master_pass.jv",'rb') as f:
        o_pwd=f.read()
    dec_pwd= encryp.decrypt_message(o_pwd)
    
    status = pwd==dec_pwd

    return status


def change(c_pwd):
    en_pwd = encryp.encrypt_message(c_pwd)
    with open("utils\\master_pass.jv",'wb') as f:
        f.write(en_pwd)


