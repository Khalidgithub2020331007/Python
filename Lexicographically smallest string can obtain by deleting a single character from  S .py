


def solve():
    input()
    a=input()
    x=a+a
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            print(a[:i]+a[i+1:])
            return
            break
    print( a[:len(a)-1])






for _ in range(int(input())):
    solve()

