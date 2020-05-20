a=[1,2,3,4,5,6,7]
even=[]
odd=[]
print("Given List",a)
for i in a:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Odd List=",odd)
print("Even List=",even)
