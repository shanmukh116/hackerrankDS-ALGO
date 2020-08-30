n=int(input())
m=list(map(int,input().split()))
k=sorted(m)
mini=999999
for i in range(len(k)-1):
    x=k[i+1]-k[i]
    if x<mini and (m.index(k[i])>m.index(k[i+1])):
        mini=x
print(mini)