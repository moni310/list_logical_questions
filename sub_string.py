list = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=list.split()
b=a
b.insert(5,"on")
b.insert(13,"on")
k=b
k.remove("over") 
k.remove("over")
print(k)