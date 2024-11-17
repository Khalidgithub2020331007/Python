


def solve():
    input()
    a=input()
    x=a+a
    for i in range(len(a)):
        x=min(x,a[:i]+a[i+1:])
    print(x)





for _ in range(int(input())):
    solve()

