list=[1,2,3,4]
name="moni"
i=0
empty=[]
while i<len(list):
    k=name+str(list[i])
    empty.append(k)
    i=i+1
print(empty,end=" ")