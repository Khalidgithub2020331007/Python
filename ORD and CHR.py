import math


def solve():
    input()
    a=input()
    arr=[]
    c=int(input())
    for i in a:
        if 'a'<=i<='z':
            b=ord(i)-ord('a')
            b=(b+c)%26
            ch=chr(b+ord('a'))
            arr.append(ch)
        elif 'A'<=i<='Z':
            b = ord(i) - ord('A')
            b = (b + c) % 26
            ch = chr(b+ord('A'))
            arr.append(ch)
        else:
            arr.append(i)
    print(''.join(map(str,arr)))




solve()

