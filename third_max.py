list1=[3,43,1,71,40,9,10,22]
i=0
m=0
while i<len(list1):
    if list1[i]>m:
        m=list1[i]
    i=i+1
ma=m
j=0
b=0
while j<len(list1):
    if list1[j]>b and list1[j]<m:
        b=list1[j]
    j=j+1
l=b
m=0
n=0
while m<len(list1):
    if list1[m]>n and list1[m]<l and list1[m]<ma:
        n=list1[m]
    m=m+1
print(n)
