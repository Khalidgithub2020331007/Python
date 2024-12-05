import heapq

def solve(b):
    min_heap = []
    max_heap = []
    a = list(map(int, input().split()))
    
    # Initialize the heaps
    for num in a:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num)  # Max-heap with negative values
    
    for _ in range(b):
        c = input()
        if len(c) > 1:
            # Insert operation
            _, e = map(int, c.split())
            heapq.heappush(min_heap, e)
            heapq.heappush(max_heap, -e)
        else:
            # Query operation
            d = int(c)
            if d == 2:
                # Get and remove the largest element
                print(-heapq.heappop(max_heap))
            else:
                # Get and remove the smallest element
                print(heapq.heappop(min_heap))

# Input
a, b = map(int, input().split())
solve(b)
