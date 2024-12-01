import sys
input = sys.stdin.read
output = sys.stdout.write

def solve():
    # Read input data
    data = sys.stdin.read().splitlines()
    t = int(data[0])  # Number of test cases

    results = []
    idx = 1
    for _ in range(t):
        n = int(data[idx])  # Number of points
        idx += 1
        a = []
        for __ in range(n):
            x, y = map(int, data[idx].split())
            a.append((x, y))
            idx += 1

        # Sort based on custom criteria
        a.sort(key=lambda p: (p[0], -p[1]))

        # Collect results
        results.extend(f"{p[0]} {p[1]}" for p in a)

    # Output all results at once
    output("\n".join(results) + "\n")

solve()
