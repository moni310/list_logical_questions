num=int(input("enter the number"))
i=0
list=[ ]
while i<=num:
    number=int(input("enter the numebr"))
    list.append(number)
    j=0
    while j<len(list):
        if list[i]<list[j]:
            k=list[i]
            list[i]=list[j]
            list[j]=k
        j=j+1
    i=i+1
print(list)
    