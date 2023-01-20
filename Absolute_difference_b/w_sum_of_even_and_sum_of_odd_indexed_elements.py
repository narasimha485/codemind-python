x=int(input())
y=list(map(int,input().split()))
os=0
es=0
for i in range(x):
    if i%2==0:
        es=es+y[i]
    else:
        os=os+y[i]
print(abs(os-es))