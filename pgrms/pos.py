n=int(input("Enter size of list:"))
li=[]
for i in range(n):
    ele=input()
    li.append(ele)
print("List is:",li)
pos=int(input("Enter position:"))
word=input("Enter a word to insert")
li.insert(pos,word)
print("Updated list:",li)
