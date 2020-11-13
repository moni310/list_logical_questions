print("your question")
q=["how many conitents are there","what is the capital of india","what you learn in ng"]
o=[["one","three","six","four"],["bhopal","mumbai","delhi","banglore"],["s.w","cleaning","cooking","leadership"]]
s=[2,3,0]
ls=[[1,2],[2,0],[0,3]]
sahi_ans=[1,3,0]
i=0
l=0
while i<len(q):
    chance=input("normal/50-50=")
    if chance=="normal":
        print("q.",i+1,q[i])
        j=0
        while j<len(o[i]):
            print(j+1,o[i][j])
            j=j+1
        user=int(input("enter the number"))
        if user==s[i]:
            print("your answer is correct") 
        else:
            print("your answer is incorrect")
            break
    elif chance=="50-50":
        if(l==0):
            print("q.",q[i])
            p=ls[i]
            print(o[i][p[0]])
            print(o[i][p[1]])
            user1=int(input("enter the number="))
            if user1==sahi_ans[i]:
                print("waoo!,your answer  is right")
            else:
                print("your answer is wrong")
                break
            l=l+1
        else:
            print("already u used")
            print("q.",q[i])
            k=0
            while k<len(o[i]):
                print(k+1,o[i][k])
                k=k+1
            user2=int(input("enter the number"))
            if user2==s[i]:
                print("you are right")
            else:
                print("you are wrong")
                break
        i=i+1


