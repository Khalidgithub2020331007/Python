import math
def solve():
  a=list(input())
  b=input()
  i,j=0,0
  while j<len(a):
    
    if a[j]==b[i]:
      i+=1 
      j+=1 
      
    elif a[j]=='?':
      a[j]=b[i]
      i+=1 
      j+=1 
    else:
      
      j+=1 
    if i==len(b):
      for i in range(len(a)):
        if a[i]=='?':
          a[i]='a'
      print('YES')
      print(''.join(a))
      
      return 
    
      
  print('NO')
  return False

for _ in range(int(input())):
  solve()
    
