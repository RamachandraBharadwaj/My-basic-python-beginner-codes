import json
import re
import random
#Welcome to MITAHARA
print("Welcome to MITAHARA")
ouser,ouser1="",""
e0,e1,e2,e3,e4,e5,e6,e7,e8,e9='0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣'
emoji=[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9]

def feedback():
    with open("feedback.json","a") as la:
        a=[]
        b=input("please give 1-5 rating : ")
        c=input("Feedback : ")
        a.append(b)
        a.append(c)
        json.dump(a,la)
def total():
    a ={}
    t=0
    with open("login.json","r") as log:
        a=json.load(log)
    for i in a:
        if ouser in i:
            t=i[ouser][1]

    print("Total Spent = ",t)
    menu()
def pickup():
    a=""
    try:
        print("Press '0️⃣' for Main Menu")
        order = []
        price = []
        exit1 = 0
        with open("restaurents.json", "r") as res:
            r = json.load(res)                    # variable r has restaurent name and menu in the form of dict
        k = 1
        list1 = []
        for i in r:                               # i will iterate key values [restautent names] of dict "r" and stores keys in list1
            list1.append(i)
            print(emoji[k], ".", i)
            k += 1
        op = int(input())                         #op is used to select restaurent
        if (op == 0):
            menu()
        r1 = list1[op - 1]                        # r1 is set to selected restaurent name(using op)
        k = 1
        list2 = []
        print("Press '0️' to order")
        for i in r[r1]:                          #now it iterates menu in that perticular restaurent and stores menu item names in list
            list2.append(i)
        for j in range(len(r[r1])):              # here oj stores menu(items or curry) of restaurent and it is helped to dispaly price of the item
            oj = list2[j]
            print(emoji[k], ".", list2[j], "=", r[r1][oj])
            k += 1
        k = 1
    except:                                      # try throws error if input is not range and exicute except
        if (op > 0):
            print("👎 No option! Try again")
            print()
            restaurents()
        else:
            print("😣 No Input")
            print()
            restaurents()
    while (exit1 == 0):
        try:
            oi = int(input())
            if (oi == 0 and len(price) != 0):
                exit1 = 1
            elif (oi == 0 and len(price) == 0):
                print("🛒Cart is Empty")
                print()
                restaurents()
            elif (oi <= len(list2)):
                qun = int(input("Enter quantity : "))
                order.append([list2[oi - 1]])
                price.append(r[r1][list2[oi - 1]] * qun)
            else:
                print("👎 No option! Try again")
        except:
            if (oi > 0):
                print("👎No option! Try again")
            else:
                print("No Input 😣")
                print("Please try again")
    print("Items Selected : ",order)
    print("Cart Price : ",sum(price))
    print("Platform fee : 30")
    print("Total amount : ",sum(price)+30)
    a=input("Press Enter to confirm...")
    if (a==""):
        order_id = ""
        for i in range(5):
            order_id += str(random.randint(0, 10))
        print()
        print("✅ Order Confirmed ")
        print("Your order id is : ", order_id)
        return 100
    else:
        print("❌ invalid input\nPlease Try again")

def reserve():
    # creating a reserve.json file and storing SEATING ARRANGEMENT and PRICES as a dictionary
    with open ("reserve.json","w+") as f:
        dict1={'2-Seater':200,'4-Seater':400,'Family Bonanza(4 - 8 members)':1400,'Private Room':2000}
        json.dump(dict1,f)
    # accesing the content previously stored in reserve.json
    with open ("reserve.json","r+") as f:
        x=json.load(f)
        #here n is a flag for the while loop about to be used
        n=0
        ee=1
        while n!='':
          #printing the dicitonary that was stored in reserve.json file
          for i in x:
              print(emoji[ee],".",i)
              ee+=1
          print("5️⃣ . Main Menu")
          #here book is a variable used to take the user's choice and the correspoinding if cases
          book=int(input("Enter your option:"))
          if book==1:
              ee=1
              option='You have chosen a 2-Seater'
              c='2-Seater'
              cost=dict1["2-Seater"]
              print(option,', Price:',cost,"\nPress 'Enter' to confirm, for cancelling enter 0️⃣")
              n=""
              n=input()
              if n=="":
                  print("✅ Seat reserved")
                  print("your seat id is : ", end="")
                  a1 = ""
                  for i in range(6):
                      a1 += str(random.randint(0, 10))
                  print(a1)
              menu()
          if book==2:
              ee=2
              option=emoji[ee],'You have chosen a 4-Seater'
              cost=dict1["4-Seater"]
              print(option,', Price:',cost,"\nPress 'Enter' to confirm, for cancelling enter 0️⃣.")
              c='4-Seater'
              n=input("")
              if n=="":
                  print("✅ Seat reserved")
                  print("your seat id is : ", end="")
                  a1 = ""
                  for i in range(6):
                      a1 += str(random.randint(0, 10))
                  print(a1)
              menu()
          if book==3:
              ee=3
              option=emoji[ee],'You have chosen Family Bonanza'
              cost=dict1["Family Bonanza(4 - 8 members)"]
              print(option,', Price:',cost,"\nPress 'Enter' to confirm, for cancelling enter 0️⃣.")
              c='Family Bonanza(4 - 8 members)'
              n=input("")
              if n=="":
                  print("✅ Seat reserved")
                  print("your seat id is : ", end="")
                  a1 = ""
                  for i in range(6):
                      a1 += str(random.randint(0, 10))
                  print(a1)
              menu()
          if book==4:
              ee=4
              option=emoji[ee],'You have chosen a Private Room'
              cost=dict1["Private Room"]
              print(option,', Price:',cost,"\nPress enter to confirm, for cancelling enter 0️⃣.")
              c='Private Room'
              n=input("")
              if n=="":
                  print("✅ Seat reserved")
                  print("your seat id is : ",end="")
                  a1=""
                  for i in range(6):
                      a1+=str(random.randint(0,10))
                  print(a1)
              menu()
          if book==5:
              menu()

def restaurents():
  try:
      print("Press '0️' for Main Menu")
      order=[]
      price=[]
      exit1=0
      with open("restaurents.json","r") as res:
        r=json.load(res)
      k = 1
      list1=[]
      for i in r:
        list1.append(i)
        print(emoji[k],".",i)
        k+=1
      op=int(input())
      if(op==0):
          menu()
      r1=list1[op-1]
      k=1
      list2=[]
      print("Press '0️' to order")
      for i in r[r1]:
        list2.append(i)
      for j in range(len(r[r1])):
        oj=list2[j]
        print(emoji[k],".",list2[j],"=",r[r1][oj])
        k+=1
      k=1
  except:
      if (op > 0):
          print("👎 No option! Try again")
          print()
          restaurents()
      else:
          print("😣 No Input")
          print()
          restaurents()
  while(exit1==0):
      try:
          oi = int(input())
          if(oi==0 and len(price)!=0):
              exit1=1
          elif(oi == 0 and len(price) == 0):
              print("🛒 Cart is Empty")
              print()
              restaurents()
          elif(oi <= len(list2)):
              qun = int(input("Enter quantity : "))
              order.append([list2[oi-1]])
              price.append(r[r1][list2[oi-1]]*qun)
          else:
              print("👎 No option! Try again")

      except:
          if(oi>0):
              print("👎 No option! Try again")
          else:
              print("😣 No Input")
              print("Please try again")

  print("Items in Cart🛒: ",order)
  print("Cart Value = ",sum(price))
  print("🚲Delivery Charges = 60")
  print("Total amount = ",sum(price)+60)
  a=input("Press Enter to confirm...")
  try:
      if(a==""):
        got=""
        with open("login.json", "r+") as lo:
            r1 = json.load(lo)
            for i in range(len(r1)):
                if(ouser in r1[i]):
                    got=r1[i]
            got[ouser][1]+=sum(price)+60
            lo.seek(0)
            json.dump(r1,lo)

        try:
            address1 = input("Enter your address : ")
            pin = int(input("Enter area pin : "))
            if (pin > 500000 and pin < 500090):
                print("✅ order confirmed")
                menu()
            else:
                print("Sorry,we are not available at your area")
                menu()
        except:
            print("Invalid address")
  except:
      address1=input("Enter your address : ")
      pin=int(input("Enter area pin : "))
      if(pin>500000 and pin<500090):
          print("✅ order confirmed")
          menu()
      else:
          print("Sorry,we are not available at your area")
          menu()

def key():
  a=0
  while(a==0):
    print("1️⃣.Login\n2️⃣.Sign up\n3️⃣.Login as gust")
    try:
      log1 = int(input())
      if(log1>0 and log1<4):
        return log1
        a=1
      else:
        print("😣 Invalid input\n")
    except:
        print("😣 Invalid input\n")


def menu():
    exit=0
    while(exit==0):
        c = 0
        while (c == 0):
          print()
          print("1️⃣.order food\n2️⃣.reserve table in hotel\n3️⃣.order and pickup from hotel\n4️⃣.Total Spent Money on Mitahara\n5️⃣.Log out")
          op = int(input())
          price = 0
          if (op == 1):
              price=restaurents()
              if(price==-100):
                  exit=100
                  c=100
              op = int(input())
          if (op == 2):
              price=reserve()

              if (price == -100):
                  exit=100
                  c = 100
              op = int(input())
          if (op == 3):
              price=pickup()
              if (price == -100):
                  exit=100
                  c = 100
              op = int(input())
          if (op == 4):
            price=total()
            if (price == -100):
                exit=100
                c = 100
            op = int(input())
          if (op == 5):
            print("Log out sucessful")
            exit=100
            c = 100
          if(op>=6):
              print("❌ Invalid input!")

def login():
  k=1
  login=dict()
  with open("login.json", "r") as log:
    login = json.load(log)
  while (k<3):
    k=key()
    if(k==1):
      c1 = 0
      with open("login.json", "r") as log:
          login = json.load(log)
      user=input("Enter E-Mail/Phone : ")
      global ouser
      ouser = user
      password=input("Enter password : ")
      ps=""
      if(c1==0):
        for i in login:
          if(user in i):
            ps=i[user][0]
            ouser1=i[user][2]
            c1=1
        if(c1==0):
          c1=80
      if(c1==1):
        if(ps==password):
          print()
          print("Hello",ouser1)
          k=menu()
          if(k==None):
            k=100
        else:
          print("❌ Wrong password")
          k=1
      else:
        print("❌ User not found\npress 2️⃣ for Sign up")
        print()

    elif(k==2):
      i=1
      while(i==1):
        w=0
        username=input("Enter your name : ")
        ouser=username
        while (True):
            user = input("Enter Phone number/mail id : ")
            try:
                user = int(user)
                user = str(user)
                x = re.search("\d{10}", user)
                if (x):
                    break
                else:
                    print("Please Enter a valid mail id or phone number")
                    continue
            except:
                if (user.endswith("@gmail.com") or user.endswith(
                        "@email.com") or user.endswith("@rediffmail.com")):
                    break
                else:
                    print("Please Enter a valid mail id or phone number")

        for j in login:
          if user in j:
            print("User already exits 🥲")
            w=1
        if(w==0):
          i=2
      password=input("Enter password : ")
      cpassword=input("Confirm password : ")
      if(len(password)>5 and len(password)<16):
          if (re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search("[0-9]",password) and re.search("[@#*$]",password)):
              if(password==cpassword):
                id = {user: [password,0,ouser]}  ############# Changed
                with open("login.json","r+") as log:
                  data=json.load(log)
                  data.append(id)
                  log.seek(0)
                  json.dump(data,log)
                print("✅ Succesfully registerd")
                print()

              else:
                print("\nPassword Mismatch❌\nTry again\n")
                k=2
          else:
              print("😣 Password should contain capital,small,number,special character")
              k=2
      else:
          print("😣 Password should contain min '6' and max '15' characters")
          k=2
    elif(k==3):
        ouser=input("Enter Your Name : ")
        print()
        print("Hello ",ouser)
        menu()
login()
feedback()