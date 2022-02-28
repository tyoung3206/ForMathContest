from ast import Not


global i ,a
def mult(n1,n2):
    if n1%2==0:
        n1=n1/2
        n2=n2+n1
        print(n1,n2)
    else:
        n2=n2/2
        n1=n1+n2
        print(n1,n2)
    while not(i==n1 and a==n2 or a==n1 and i==n2):
        # print(i,a)
        if n1%2==0:
            n1=n1/2
            n2=n2+n1
            print(n1,n2)
        else:
            n2=n2/2
            n1=n1+n2
            print(n1,n2)




i=input("第一個數?")
i=int(i)
a=input("第二個數?")
a=int(a)
mult(i,a)
