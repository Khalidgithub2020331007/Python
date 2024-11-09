

input()
a=list(map(int,input().split()))
m={}
for i in a:
    if i in m:
        m[i]+=1
    else:
        m[i]=1
c=0
for i,j in m.items():
    c+=m[i]%i
print(c)

