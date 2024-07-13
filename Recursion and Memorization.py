a=[0]*(10010)
mod=int(1e9+7)
def fact(n):
    global a,mod
    if n==0:
        a[0]=1
        return a[0]
    else:
        a[n]=(n*fact(n-1))%mod
        return a[n]
n=int(input())
(fact(n))
for i in range(n+1):
    print(a[i],end=' ')
