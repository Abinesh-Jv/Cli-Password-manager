import os

def main():
    while True:
        print("\tMENU\n1.Generate password\n2.Save password\n3.Show password\n4.Delete password\n5.Change Settings\n6.Exit")
        ch=input("Enter your choice(1/2/3) : ")
        if ch.isdigit() and int(ch) in [1,2,3,4,5,6]:
            ch=int(ch)
            break

        else:
            print("\tInvalid Input!!\n")
    os.system("cls")
    return ch
    

