n=int(input())
d_li=[]
u_li=[]
for i in range(0,n):
    ele=int(input())
    d_li.append(ele)
print("duplicate list:",d_li)
sum=0
for num in d_li:
    sum+=num
print(sum)
for num in d_li:
    if num not in u_li:
        u_li.append(num)
print("unique list:",u_li)
