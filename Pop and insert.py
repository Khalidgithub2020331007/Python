n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    for j in range(len(a)):
        if(i==a[j]):
            print(j+1,end=' ')
            a.pop(j)
            a.insert(0,i)
            break
