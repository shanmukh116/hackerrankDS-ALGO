n=int(input())
for i in range(n):
    k=int(input())
    a=list(map(int,input().split()))
    f=[]
    l,h=0,len(a)-1
    for i in range(len(a)//2):
        if(l<h):
            f.append(a[h])
            f.append(a[l])
            h-=1
            l+=1
    if(len(a)%2==1):
        f.append(a[len(a)//2])
    for i in range(len(f)):
        print(f[i],end=" ")
    print(end="\n")  