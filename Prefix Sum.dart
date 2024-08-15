nums=list(map(int,input().split()))
a=[]
a.append(0)
for i in range(len(nums)):
  a.append(a[i]+nums[i])
print(a)
