x=int(input())
y=list(map(int,input().split()))
s=0
for i in range(x):
    if i%2==0:
        s=s+y[i]
print(s)