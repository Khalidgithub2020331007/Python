for _ in range(int(input())):
    n=int(input())
    a=input()
    s=[]
    s.append(a[0])
    for i in range(1,n):
        if(a[i]=='A'and len(s)!=0):
            if(s[len(s)-1]=='Q'):
                s.pop()
        if(a[i]=='Q'):
            s.append('Q')
    if(len(s)==0):
        print('YES')
    else:
        print('NO')
