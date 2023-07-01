#matrix multiplication


def matro(x,y):
    gg=[]
    print("enter the matrix elements")
    for i in range(x):
        tempo=[]
        for j in range(y):
            a=int(input())
            tempo.append(a)
        gg.append(tempo)

    return gg
        
r1=int(input("enter the number of rows of the matrices"))
c1=int(input("enter the number of columns of the matrix"))

mat1=matro(r1,c1)

r2=int(input("enter the number of rows of the matrices"))
c2=int(input("enter the number of columns of the matrix"))

mat2=matro(r2,c2)

print(mat1)
print(mat2)

if(c1!=r2):
    print("matrix multiplication not possible")
else:
    mult=[]
    for i in range(r1):
        tempo=[]
        for j in range(c2):
            su=0
            for k in range(c1):
                pro=mat1[i][k]*mat2[k][j]
                su+=pro
            tempo.append(su)
        mult.append(tempo)


print(mult)
