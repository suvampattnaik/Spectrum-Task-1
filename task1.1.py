def parameters():
    a=int(input("Enter num 1:"))
    b=int(input("Enter num 2:"))
    def sum(x,y):
        z=x+y
        return z
    c=sum(a,b)+5
    return c
print("Sum after adding 5=",parameters())
