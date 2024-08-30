from operator import truediv


def f(i,mymap):

    for j in range(1,len(a)):
        b=i[:j]
        c=i[j:]
        if b in mymap and c in mymap:
            return '1'

    return '0'






for _ in range(int(input())):
    a=[]
    mymap={}
    for _ in range(int(input())):
        value=input()
        a.append(value)
        mymap[value]=1
    # for key,values in mymap.items():
    #     print(key,values,end='  ')
    # print()
    b=[]
    for i in a:
        b.append(f(i,mymap))
    print(''.join(b))
