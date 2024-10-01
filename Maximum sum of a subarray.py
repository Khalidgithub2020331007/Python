def solve():
    input()  # Skip the length of the array
    arr = list(map(int, input().split()))  # Convert input to list of integers
    current_sum = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
        
    print(max_sum)


for _ in range(int(input())):
    solve()
