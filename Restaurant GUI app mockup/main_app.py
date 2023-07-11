import json
from functools import partial
import customtkinter as ct
import tkinter as tk
from CTkMessagebox import CTkMessagebox

win=ct.CTk()
win.title("Restaurant Menu")
win.geometry("860x640")
win.resizable(False,False)

fl=0
tr=None
scroll_flag=None
item_prev=None
val=0
ent=[]
quantity=[]
obj_list=[]
quan_dict={}
k=0
bookin=[]

z=0

tabs=ct.CTkTabview(win,width=860,height=600)
tabs.pack(padx=100,pady=80)
tabs.add("login/registration")
tabs.add("browse")
tabs.add("cart")

tabs.set("login/registration")

dict1={'1. 2-Seater':200,'2. 4-Seater':400,'3. Family Bonanza(4 - 8 members)':1400,'4. Private Room':2000}


def bill_calc(keyo):
    global bookin
    global hotels
    global dict1
    global quan_dict
    
    total=0.0

    ido=int(bookin[0])-1
    
    bill_win=ct.CTkToplevel(win)
    bill_win.geometry("400x300")
    bill_win.resizable(0,0)
    bill_win.title("Your Bill !")
    bill_win.configure(fg_color="#b6e3c6")
    bill_win.attributes('-topmost', 'true')

    val=0
    hem=0

    res_fr=ct.CTkFrame(bill_win,height=50,width=350)
    res_fr.pack()

    res_str=ct.StringVar()
    res_str=str(list(dict1.keys())[ido])+"\t Rs. "+str(list(dict1.values())[ido])
    print(res_str)
    

    res_lab=ct.CTkLabel(res_fr,text=res_str,font=("Roboto",16))
    res_lab.pack(padx=10,pady=10)

    item_fr=ct.CTkFrame(bill_win,height=500,width=400)
    item_fr.pack()

    for idx,i in enumerate(hotels[keyo].items(),val):
        for j in quan_dict.items():
            if(idx==j[0]):
                ke=i[0]
                total+=j[1]*hotels[keyo][ke]


    tax=(5/100)*total

    total_lab=ct.CTkLabel(res_fr,text="item costs: \tRs. "+str(total),font=("Roboto",20))
    total_lab.pack(pady=20,padx=10)

    tax_lab=ct.CTkLabel(res_fr,text="GST costs: \tRs. "+str(tax),font=("Roboto",20))
    tax_lab.pack(pady=20)

    grand_total=tax+total+(list(dict1.values())[ido])

    gran_lab=ct.CTkLabel(res_fr,text="Grand Total= \tRs. "+str(grand_total),font=("Roboto",20))
    gran_lab.pack(pady=20)

def cart_disp(dictio,keyo):
    global pl_fr
    global z
    global hotels    
    global obj_list
    if(obj_list):
        for i in obj_list:
            i.pack_forget()
    
    ite=ct.StringVar()

    if(z==0):
        bill_but=ct.CTkButton(tabs.tab("cart"),text="procced with bill",text_color="black",command=partial(bill_calc,keyo))
        bill_but.pack(side="bottom")
        z+=1

    for i in dictio.items():
        a=i[0]
        b=i[1]
        ite=list(hotels[keyo].items())[a]
                              
        sub_fr=ct.CTkFrame(pl_fr,height=100,fg_color="#2b2b2b")
        sub_fr.pack()
        
        item_lab=ct.CTkLabel(sub_fr,text=ite,font=("Arial",20,"bold"))
        item_lab.pack(side="left")

        quantity_lab=ct.CTkLabel(sub_fr,text=("quantity : "+str(b)),font=("Arial",20,"bold"))
        quantity_lab.pack()
        
        obj_list.append(sub_fr)
        


def cart_calc(m,entryy):
    global quantity
    global quan_dict
    
    quantity.append(m)
    print(quantity)
    uniq_sel=set(quantity)
    for i in uniq_sel:
        quan_dict.update({i:quantity.count(i)})

    #print(quan_dict)
    cart_disp(quan_dict,entryy)
    

def reserv(r):
    cx=""
    option=""
    optnum={"1","2","3","4"}
    global dict1
    global bookin

    bookin=[]
    
    book=str(r.get())
    lab_mes=ct.StringVar()
    print(book)
    if book=="1":
        option='You have chosen a 2-Seater'
        lab_mes=option
        cx='1. 2-Seater'
        cost=dict1["1. 2-Seater"]
              
    if book=="2":
        option='You have chosen a 4-Seater'
        cost=dict1["2. 4-Seater"]
        lab_mes=option
        cx='2. 4-Seater'
        
    if book=="3":
        option='You have chosen Family Bonanza'
        cost=dict1["3. Family Bonanza(4 - 8 members)"]
        lab_mes=option
        cx='3. Family Bonanza(4 - 8 members)'
        
    if book=="4":
        option='You have chosen a Private Room'
        cost=dict1["4. Private Room"]
        lab_mes=option
        cx='4. Private Room'

    if(book not in optnum ):
        CTkMessagebox(title="Input error !", message="Enter only from reservation options!",icon="warning",button_text_color="black")
        book=0
    else:
        CTkMessagebox(title="reservation successful",message=option)


    bookin.append(book)

def browse():
    
    global fl
    if(fl==0):
        global not_log
        global not_log_mes
        global dict1
    
        not_log.destroy()
        not_log_mes.destroy()
        
        with open ("reserve.json","w+") as f:
            json.dump(dict1,f) 

        dis_op=ct.StringVar()

        opt_fr=ct.CTkFrame(tabs.tab("browse"),width=200,height=200)
        opt_fr.pack(padx=8)

        for i in dict1.keys():
            dis_op=i
            op_lab=ct.CTkLabel(opt_fr,text=dis_op)
            op_lab.pack(side="left")

        res_ent=ct.CTkEntry(opt_fr,width=200)
        res_ent.pack(pady=10,padx=5,side="bottom")

        reser=ct.CTkButton(opt_fr,text="reserve seats",text_color="black",command=partial(reserv,res_ent))
        reser.pack(pady=10,padx=5,side="bottom")
        

        sec_fr=ct.CTkFrame(tabs.tab("browse"),width=400,height=400)
        sec_fr.pack(pady=10,padx=6)
        
        enter=ct.CTkEntry(sec_fr,placeholder_text="Enter the restaurant name ",width=300)
        enter.pack(padx=40,pady=10)

        give=ct.CTkButton(sec_fr,text="go!",command=lambda: accept(enter),text_color="black")
        give.pack(pady=10)        

        fl+=1
    
def authenticate(k):
    #global login_tab
    #global reg_tab
    global pl_fr

    #login_tab.destroy()
    #reg_tab.destroy()
    
    print(k)
    print(ent)
    ans=""
    pair=[]

    for i in ent:
        try:
            val=str(i.get())
            pair.append(val)
            i.delete(0,tk.END)
        except:
            del i
            continue
    print(pair)

    with open("login.json", "r") as log:
        login = json.load(log)

    if(k==1):
        c1=0
        ps=""
        print(login)

        for i in login:
            if(pair[0] in i):
                ps=i[pair[0]]
                c1=1
            if(c1==0):
                c1=80
        if(c1==1):
            if(ps==pair[1]):
                CTkMessagebox(title="Login successful !", message="welcome,{} !".format(pair[0]),icon="check",button_text_color="black")
                pl_fr.pack()
                #login_tab.destroy()
                browse()
                #message box login successful and destroy the login tab
            else:
                #message box of invalid details. wrong password
                CTkMessagebox(title="Invalid details", message="Wrong password! Authentication failed",icon="cancel",button_text_color="black")
                k=1
        else:
            CTkMessagebox(title="Attention", message="This user doesn't exist!",icon="warning",button_text_color="black")

    if(k==2):
        j=1
        l=len(login)
        for i in range(l):
            if(pair[0] in login[i]):
                CTkMessagebox(title="Sign-up Error", message="This user already exists!",icon="cancel",button_text_color="black")
                j=5
        
        if(j!=5):
            if(pair[1]==pair[2]):
                ido={pair[0]:pair[1]}
                with open("login.json","r+") as log:
                    data=json.load(log)
                    data.append(ido)
                    log.seek(0)
                    json.dump(data,log)
                CTkMessagebox(title="registration",message="Registration successful!!",icon="check",button_text_color="black")
        


    
def registration():
    #global k
    k=2
    reg_tab=ct.CTkToplevel(win)
    reg_tab.resizable(0,0)
    reg_tab.title("registration details")
    reg_tab.geometry("300x300")
    reg_tab.configure(fg_color="#b6e3c6")
    reg_tab.attributes('-topmost', 'true')
    
    reg_frame=ct.CTkFrame(reg_tab,width=280,height=280)
    reg_frame.pack()
    
    userlab=ct.StringVar()
    userlab.set("Username : ")
    userna=ct.CTkLabel(reg_frame,textvariable=userlab,height=4)
    userna.place(relx=0.1,rely=0.2)

    username_in=ct.StringVar(None)
    username_in=ct.CTkEntry(reg_frame,textvariable=username_in,width=100)
    username_in.place(relx=0.6,rely=0.2)
    ent.append(username_in)

    passlab=ct.StringVar()
    passlab.set("Password : ")
    passwo=ct.CTkLabel(reg_frame,textvariable=passlab,height=4)
    passwo.place(relx=0.1,rely=0.4)

    password_in=ct.StringVar(None)
    password_in=ct.CTkEntry(reg_frame,textvariable=password_in,width=100)
    password_in.place(relx=0.6,rely=0.4)
    ent.append(password_in)

    conpasslab=ct.StringVar()
    conpasslab.set("Confirm Password : ")
    conpasswo=ct.CTkLabel(reg_frame,textvariable=conpasslab,height=4)
    conpasswo.place(relx=0.1,rely=0.6)

    conpassword_in=ct.StringVar(None)
    conpassword_in=ct.CTkEntry(reg_frame,textvariable=conpassword_in,width=100)
    conpassword_in.place(relx=0.6,rely=0.6)
    ent.append(conpassword_in)

    #need to add command argument here
    submit_but_reg=ct.CTkButton(reg_frame,text="enter",text_color="black",command=partial(authenticate,k))
    submit_but_reg.place(relx=0.3,rely=0.8)

    #reg_tab.protocol("WM_DELETE_WINDOW", reg_tab.destroy())


def login():
    global k

    k=1
    login_tab=ct.CTkToplevel(win)
    login_tab.resizable(0,0)
    login_tab.attributes('-topmost', 'true')

    login_tab.title("login details")
    login_tab.geometry("300x300")
    login_tab.configure(fg_color="#b6e3c6")
    
    login_frame=ct.CTkFrame(login_tab,width=280,height=280)
    login_frame.pack()
    
    userlab=ct.StringVar()
    userlab.set("Username : ")
    userna=ct.CTkLabel(login_frame,textvariable=userlab,height=4)
    userna.place(relx=0.1,rely=0.2)

    username_in=ct.StringVar(None)
    username_in=ct.CTkEntry(login_frame,textvariable=username_in,width=100)
    username_in.place(relx=0.6,rely=0.2)
    ent.append(username_in)

    passlab=ct.StringVar()
    passlab.set("Password : ")
    passwo=ct.CTkLabel(login_frame,textvariable=passlab,height=4)
    passwo.place(relx=0.1,rely=0.6)

    password_in=ct.StringVar(None)
    password_in=ct.CTkEntry(login_frame,textvariable=password_in,width=100)
    password_in.place(relx=0.6,rely=0.6)
    ent.append(password_in)

    submit_but_log=ct.CTkButton(login_frame,text="enter",text_color="black",command=partial(authenticate,k))
    submit_but_log.place(relx=0.3,rely=0.85)

    #login_tab.protocol("WM_DELETE_WINDOW", login_tab.destroy())
    #ct.Toplevel.winfo_exists(login_tab)


c=0

#fonts -Poor Richard
ct.set_default_color_theme("E:\\Coding guide\\Audi proj w somanath and anurag\\bihlana.json")
win.configure(fg_color="#b6e3c6")

#ct.set_default_color_theme("light")
head=ct.CTkLabel(tabs.tab("login/registration"),
                 text="Mitahara",
                 font=("Vivaldi",90),
                 fg_color="#2b2b2b",
                 text_color="yellow",
                 #corner_radius=100
                 compound="bottom")
head.pack(padx=20,pady=(30,20))

def menu(hotel_na):
    global err_label
    global tr
    global item_prev
    global scroll_flag
    global val

    opscroll.pack()
    
    if(hotel_na in hotels):
        scroll_flag=True
        if(tr==True):
            err_label.destroy()
            
        opscroll.pack()

        if(item_prev):
            opscroll.pack_forget()

        for idx,i in enumerate(hotels[hotel_na].items(),val):
            item_prev=True
            
            scroll_fr=ct.CTkFrame(opscroll,width=1000,height=200)
            scroll_fr.pack(pady=10)
            
            item_name=ct.CTkLabel(scroll_fr,text=i[0],text_color="white",font=("Arial",20))
            item_name.pack(side="right",padx=2)

            item_price=ct.CTkLabel(scroll_fr,text=i[1],font=("Arial",15))
            item_price.pack(padx=5,side="right")

            add_cart=ct.CTkButton(scroll_fr,text_color="black",text="Add to Cart",command=partial(cart_calc,idx,hotel_na))
            add_cart.pack(padx=2,side="right")

            
            #add_cart.pack(padx=40)
            
            print(i)
    if(hotel_na not in hotels):
        if(scroll_flag):
            opscroll.pack_forget()
        tr=True
        scroll_flag=False
        err_label=ct.CTkLabel(tabs.tab("browse"),text="restaurent not found",font=("Arial",20,"italic"))
        err_label.place(relx=0.35,rely=0.65)    

   
fr=ct.CTkFrame(tabs.tab("login/registration"),width=200,height=200)
fr.pack()

line=ct.CTkLabel(fr,text="choose your next meal from the variety of best options we provide !",font=("Arial",20,"italic"))
line.pack()

logbut=ct.CTkButton(tabs.tab("login/registration"),
                             text="login",
                            text_color="black",
                             command=login
                             )
logbut.pack(pady=20)


regbut=ct.CTkButton(tabs.tab("login/registration"),
                    text="register",
                    text_color="black",
                    fg_color="#42b4ed",
                    command=registration
                    )

regbut.pack(pady=10)

def accept(e):
    global c
    hotel_na=e.get()
    c+=1
    #if(c==1):
    menu(hotel_na)
    print(hotel_na)

opscroll=ct.CTkScrollableFrame(tabs.tab("browse"),width=900,height=600)

not_log=ct.CTkLabel(tabs.tab("browse"),text="Not Logged in !",font=("Poor Richard",30))
not_log.pack()

not_log_mes=ct.CTkLabel(tabs.tab("browse"),text="enter the username and password to explore the market place",font=("Helvetica",15,"italic"))
not_log_mes.pack()

carto=ct.CTkLabel(tabs.tab("cart"),text="items in cart :",font=("MS Sans Serif",20),)
carto.pack(side="top",pady=10)

with open("restaurants.json","r") as rem:
    hotels=json.load(rem)
    #print(hotels)

err_label=ct.CTkLabel(tabs.tab("cart"))

pl_fr=ct.CTkFrame(tabs.tab("cart"),height=400,width=760,fg_color="#2b2b2b")

win.mainloop()
