x=int(input())
y=list(map(int,input().split()))
s=0
for i in y:
    if i%2==1:
        s=s+i
print(s)