from src import encryp
from os import system
from src.mas_pswd import check,change
from time import sleep
def main():
    system("cls")
    mp = input("Enter the master password : ")
    if check(mp):
        new_pwd = input("Enter your new password : ")
        change(new_pwd)
    else :
        print("Wrong password!!")
        print("Closing in 3s")
        sleep(2)







if __name__ == '__main__':
    main()
