S1=[1,2,3,4,5,6,7,8,9]
S2=[1,3,4,6,8,11,22,34,51,67]
a=[]
for i in S1:
    if i not in S2:
        a.append(i)
print("S1:",a)