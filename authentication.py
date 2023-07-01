def login():
    global maidict
    req=""
    x=input("Enter the username to login : ")
    print(maidict.keys())
    
    if x in maidict.keys():
        y=input("Enter the password to login : ")
        req=maidict[x]
        print(req)
        if(req==y):
            print("Login succesful !")
        else:
            print("wrong password !")
    else:
        print("Invalid username !")
        

def registration():
    global maidict
    n=input("Enter the username to be registered : ")
    p=input("Enter the password to be registered : ")
    maidict.update({n:p})
    
def invalid():
    print("Invalid input")

def display():
    print("Enter 1 for login \nEnter 2 for registration")
    n=int(input())
    return n
 
        
maidict={}
print("Welcome to Main Menu")
des=display()
if(des==1):
    login()
elif(des==2):
    registration()
    display()
    login()
else:
    invalid()


