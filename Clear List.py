


def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    b=[]
    c=[0]
    f='+'
    a=''
    for i in range(n):
        if arr[i]<0:
            a='-'
        else:
            a='+'
        if f==a:
            c.append(arr[i])
        else:
            m=max(c)
            b.append(m)
            del c[:]
            c.append(arr[i])
            f=a
    m = max(c)
    b.append(m)
    print(sum(b))





for _ in range(int(input())):
    solve()
