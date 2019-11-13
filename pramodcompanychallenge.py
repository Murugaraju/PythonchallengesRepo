a='[fgdgdgdgdgdgdgddg][[]][]]'

flag=False
count=0
for i in a:
    if i=='[' or flag:
        if not flag:
            flag=True
        if i=='[':
            continue
        if i==']':
            flag=False
            count+=1
            continue
           
        print(i)
        
        
print("printing count ---->",count)
        
