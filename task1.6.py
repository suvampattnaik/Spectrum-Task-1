a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
n=int(input("Enter 1 for Sum,2 for Substraction,3 for Multiplication,4 for Division:"))
def sum():
    c=a+b
    return c
def substract():
    d=a-b
    return d
def multiply():
    e=a*b
    return e
def divide():
    f=a/b
    return f
if n==1:
    print("Result=",sum())
elif n==2:
    print("Result=",substract())
elif n==3:
    print("Result=",multiply())
elif n==4:
    print("Result=",divide())
