shifts=list(map(int,input().split()))
b=[]
b.append(0)
for i in range(len(shifts)-1,-1,-1):
    a=b[0]+shifts[i]
    b.insert(0,a)
print(b)
