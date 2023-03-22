import ast

def main():


    with open("config\\settings.jv",'r') as f:
        config = f.read()
    config = ast.literal_eval(config)
    key_list = list(config.keys())
    val_list = list(config.values())
    for i in range(len(config)):
        print(f"{i+1}.{key_list[i]} : {val_list[i]}")
    point = True

    while True:
        while True:
            cha=input("Change(1/2/3) or 0 to Exit : ")
            if cha.isdigit and cha !="":
                cha=int(cha)
                break
            else:
                print("Invalid")
                continue
        if cha == 1:
            while True:
                length=input("Enter the length (greater than 4) : ")
                if length.isdigit() and int(length)>=4:
                    length=int(length)
                    break
                else:
                    print("Invalid")
                    continue
            val_list[0]=length
            break
        
        elif cha in [2,3]:
            val_list[cha-1] = not(val_list[cha-1])
            break
        elif cha == 0:
            point = True
            break
        else:
            print("Invalid")
            continue
    
    new_settings = dict(zip(key_list,val_list))
    new_settings = str(new_settings)
    with open("config\\settings.jv",'w') as f:
        f.write(new_settings)


    if point:
        return point
    else :
        return not point
    
def get_data():
    with open("config\\settings.jv",'r') as f:
        config = f.read()
    config = ast.literal_eval(config)
    val_list = list(config.values())
    
    return val_list[0],val_list[1],val_list[2]
    


