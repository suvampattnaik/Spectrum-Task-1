sample={'Physics':88,'Maths':75,'Chemistry':72,'Basic Electrical':89}
print("Given dictionary:",sample)
a= min(sample.values())
for i in sample:
    if (sample[i]== a):
        print("Key corresponding to minimum value is:",i)


