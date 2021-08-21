list=[3,7,3,5,4,3]
i=0
while i<len(list):
    j=0
    count=0
    while j<len(list):
        if list[i]==list[j]:
            num=list[j]
            count=count+1
        j=j+1
    i=i+1
counter=count
if counter >=3:
    print(num,counter)
else:
    pass
