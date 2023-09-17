def convo(x):
    c=0
    global l
    global n
    re=0
    word=""
    if(l<=4):
        while(x!=0):
            te=""
            z=re
            re=x%10
            if(re==1 and c==1):
                te=spl[z]
                word=""
                word=te+" "+word
                c+=1
                x=x//10
                continue

            if(re==0):
                c+=1
                x=x//10
                continue
            if(c!=1):
                te=numbers[0][re]
                if(c==2):
                    te=te+" hundred "
                if(c==3):
                    te=te+" thousand "
                word=te+word
            else:
                te=numbers[1][re]
                word=te+" "+word
            c+=1
            x=x//10
        print(word)
    else:
        print("Length more than 4 is not supported")
            
    
    
n=input("Enter a number:")
l=len(n)
numbers=[["","one","two","three","four","five","six","seven","eight","nine"],["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]]
spl=["ten","eleven","twelve","thierteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
try:
    x=int(n)
    match x:
        case 0:
            print("zero")
        case 10:
            print("ten")
        case 100:
            print("hundred")
        case 1000:
            print("thousand")
        case _:
            convo(x)

except:
    print("Invalid input")
