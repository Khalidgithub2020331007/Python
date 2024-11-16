import itertools

def solve():
    n=int(input())
    numbers = list(range(1, n + 1))

    permutations = itertools.permutations(numbers)

    # Print each permutation
    arr=[]
    for perm in permutations:
        arr.append(list(perm))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    aa=0
    bb=0
    for i in range(len(arr)):
        if arr[i]==a:
            aa=i
        if arr[i]==b:
            bb=i
    print(abs(aa-bb))


solve()
