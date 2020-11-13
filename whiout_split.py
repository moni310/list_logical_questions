list= "i am student"
i=0
empty=[]
space=" "
while i<len(list):
    if list[i]==" ":
        empty.append(space)
        space=" "
    else:
        space=space+list[i]
    i=i+1
print(empty)