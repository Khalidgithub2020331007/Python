
def main():
    # Optimize input/output (Python equivalent)
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Parse input
    n, q = map(int, data[0].split())
    a = list(map(int, data[1:n+1]))

    # Queries processing
    result = []
    for i in range(n+1, n+q+1):
        x = int(data[i])

        lo = -1
        l, r = 0, n-1

        # Binary search
        while l <= r:
            mid = (l + r) // 2

            if a[mid] >= x:
                lo = mid
                r = mid - 1
            else:
                l = mid + 1

        if lo == -1:
            lo = n
        
        result.append(lo)

    # Output all results at once for faster performance
    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
