n=int(input())
f=0
s=1
print(f)
print(s)
temp=0
for i in range(2,n):
    temp=f+s
    f=s
    s=temp
    print(temp)
