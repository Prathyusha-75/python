st=input()
word=st.split()
if len(word)>=2:
    second=word[1].upper()
    print(second)
else:
    print("not enough words")
