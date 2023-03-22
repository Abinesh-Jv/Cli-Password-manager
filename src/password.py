import os
import random
import string
from src.decor import encrypt
import ast
from src import encryp

@encrypt
def generate(lim,num=True,punc=True):
    letters = string.ascii_letters
    numbers = string.digits
    sp_chars = string.punctuation
    
    chars = letters
    if num:
        chars+=numbers
    if punc:
        chars+=sp_chars
    pwd=''
    
    for i in range(lim):
        if i < 3:
            if num and not punc:
                if i == 0:
                    pwd+=random.choice(letters)
                elif i == 1:
                    pwd+=random.choice(numbers)
            elif not num and punc:
                if i == 0:
                    pwd+=random.choice(letters)
                elif i == 1:
                    pwd+=random.choice(sp_chars)
            elif num and punc:
                if i == 0:
                    pwd+=random.choice(letters)
                elif i == 1:
                    pwd+=random.choice(numbers)
                elif i==2:
                    pwd+=random.choice(sp_chars)
        else:
            pwd+=random.choice(chars)


    return pwd

def pwd_collector():
    with open("data\\data.jv",'rb') as f:
        all_pwd = f.read()
    all_pwd = encryp.decrypt_message(all_pwd)
    all_pwd = ast.literal_eval(all_pwd)
    return all_pwd


def insert(psd,new):
    if new:
        ins = True
    else:
        insert_status=input("Would you like to save this password (y/n) ").lower()
        if insert_status == 'n':
            return False
        elif insert_status == 'y':
            ins = True
        elif insert_status == "":
            return False
        else:
            return
    while ins:
            while True:
                name = input("Name of the password : ")
                if name == "":
                    continue
                else:
                    name = name.lower()
                    break
            if name == "exit":
                print("You can't have that name!")
                continue
            every_pwd = pwd_collector()
            if name in every_pwd:
                print("Already Exists!")
            else:
                break

    every_pwd[name] = psd
    every_pwd = encryp.encrypt_message(str(every_pwd))
    with open("data\\data.jv","wb") as f:
        f.write(every_pwd)

def show_pwd():
    pwd=pwd_collector()
    key_list = list(pwd.keys())
    val_list = list(pwd.values())
    for i in range(len(pwd)):
        print(f"{key_list[i].capitalize()} : {val_list[i]}")
    _ = input("Press Enter to exit")

def delete_pwd():
    pwd=pwd_collector()
    key_list = list(pwd.keys())
    val_list = list(pwd.values())
    for i in range(len(pwd)):
        print(f"{key_list[i].capitalize()} : {val_list[i]}")
    while True:
        while True:
            delete_pwd = input('password you wants to delete (Enter "exit" to Exit) : ')
            if delete_pwd == "":
                continue
            else:
                delete_pwd = delete_pwd.lower()
                break
        if delete_pwd in pwd:
            del pwd[delete_pwd]
            pwd = encryp.encrypt_message(str(pwd))
            with open("data\\data.jv","wb") as f:
                f.write(pwd)
            break
        elif delete_pwd.lower() == "exit":
            break

        else:
            pass

def save_new_password():
    os.system("cls")
    while True:
        passwd = input("Enter Your password : ")
        if passwd == "":
            continue
        else:
            break

    insert(passwd,True)



    
    



if __name__ == '__main__':
    insert("blablabla")

