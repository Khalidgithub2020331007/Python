from collections import defaultdict


def solve():
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    mm=defaultdict(list)
    for i in range(n):
        mm[arr[i]].append(i+1)
    # print(mm)
    arr.sort()
    i=0
    c=0
    while(i<n):
        d=mm[arr[i]].pop(0)
        if k>=d+arr[i]:
            c+=1
            k=k-d-arr[i]

        i+=1
    print(c)
for i in range(int(input())):
    solve()
