a="AaBbCcDdEeFfGgHhIijKLMN"
print("Given Character:",a)
print("Arrangement of the characters:")
def lower():
    for i in a:
        if i.islower():
            print(i,end=",")
def upper():
    for j in a:
        if j.isupper():
            print(j,end=",")

lower()
upper()



