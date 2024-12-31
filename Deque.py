from collections import deque
q=deque()
for _ in range(int(input())):
    a=input()
    if a[5]=='b':
        b,cc=map(str,a.split())
        c=int(cc)
        q.append(c)
    if a[5]=='f':
        b,cc=map(str,a.split())
        c=int(cc)
        q.appendleft(c)
    if a[5]=='r':
        if len(q)==0:
            print('Empty')
        else:
            print(q.popleft())
    if a[5]=='a':
        if len(q)==0:
            print('Empty')
        else:
            print(q.pop())
    # print(q)


