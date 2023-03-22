import random
import os
import time
from src import mas_pswd,settings
from src import password,ui
import ast

def main():
    while True:
        os.system('cls')
        mp=input("Enter the Master Password : ")
        if mas_pswd.check(mp):
            while True:
                os.system("cls")
                val = ui.main()
                pas_len,ne_num,ne_ch = settings.get_data()
                if val == 1:
                    os.system("cls")
                    en_pwd,pwd = password.generate(pas_len,ne_num,ne_ch)
                    print(pwd)
                    password.insert(pwd,False)
                elif val == 2:
                    password.save_new_password()
                elif val == 3:
                    password.show_pwd()
                elif val == 4:
                    password.delete_pwd()
                elif val == 5:
                    settings.main()
                elif val == 6:
                    quit()
        else :
            continue
        





if __name__=='__main__':
    main()


