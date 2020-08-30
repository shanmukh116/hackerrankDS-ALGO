n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(len(b)):
    if b[i] in a:
        a.remove(b[i])
    else:
        k.append(b[i])
k=set(k)
k=list(k)
k.sort()
m=map(str,k)
print(" ".join(m)) 