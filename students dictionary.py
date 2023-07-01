imp={}
fin={}
rf={}


def ipu():
    global imp
    try:
        n=int(input("Enter the number of students  whose data must be accepted"))
    except:
        print("invalid input")
    x=1

    while(x<=n):
        a=input("Enter the roll number of the student : ")
        b=[]*3
        print("Enter the marks of the three subjects - ")
        for i in range(1,4):
            print(i,".",end=" ")
            b.append(int(input()))
        imp.update({a:b})

        x+=1



def calc():
    global imp
    fin={}
    for i,j in imp.items():
        gpa=0.0
        su=0
        for x in j:
            su+=x
        gpa=su/3

        fin.update({i:gpa})
        

def sorto():
    global fin
    global rf
    for i,j in fin



    
ipu()



