n, m = map(int, input().split())
a = list(map(int, input().split()))

# Initialize prefix sum list
s = [0]

# Compute prefix sums
for i in a:
    s.append(s[-1] + i)

# Initialize hashmap to count prefix sums
myMap = {0: 1}
cnt = 0

# Check for subarrays with sum equal to m
for i in range(1, len(s)):
    b = s[i] - m
    if b in myMap:
        cnt += myMap[b]
    if s[i] in myMap:
        myMap[s[i]] += 1
    else:
        myMap[s[i]] = 1

print(cnt)
