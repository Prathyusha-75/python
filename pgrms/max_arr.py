n=int(input())
arr=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
print(arr)
max=0
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)
