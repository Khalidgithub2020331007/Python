
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()
    o=[]
    z=[]
    c=0
    print(s)
    if s[len(s)-1]=='0':
        s=(s+'1')
    else:
        s=(s+'0')
    print(s)
    for i in range(len(s)-1):
        if s[i]=='0':

            c+=1
        if s[i]=='0' and s[i+1]=='1':
            z.append(c)
            c=0
    c=0
    for i in range(len(s)-1):
        if s[i]=='1':
            c+=1
        if s[i]=='1' and s[i+1]=='0':
            o.append(c)
            c=0
    print(z,o)

