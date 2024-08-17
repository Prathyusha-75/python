st=input()
max_f={}
for i in st:
    if i in max_f:
        max_f[i]+=1
    else:
        max_f[i]=1
result=min(max_f,key=max_f.get)
print(result)
