l=[1,2,2,4,4]
l1=[]
l2=[]
for i in range(len(l)):
        l2=[]
        l2.append(l[i])
        l2.append(l[i+1])
        l1.append(l2.copy())
print(l1) 
    
