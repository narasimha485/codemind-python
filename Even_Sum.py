x=int(input())
y=list(map(int,input().split()))
s=[]
for i in y:
    if i%2==0:
        s.append(i)
print(sum(s))
