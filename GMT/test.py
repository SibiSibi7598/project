import numbers


def table(n,t):

    if n!=0:
        table(n-1,t)
        print(n,"*",t,"=",n*t)
    
n=int(input("enter the numbers"))
t=int(input("enter the table"))
table(n,t)