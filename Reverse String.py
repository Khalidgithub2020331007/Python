a=int(input())
s=""
while( a!=1):
    if(a%2==1):
        s+='1'
    else:
        s+='0'
    a=int(a/2)
s+="1"
s=s[::-1]
print(s)
