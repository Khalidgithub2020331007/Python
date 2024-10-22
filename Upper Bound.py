import bisect

def main():
    v = [3, 4, 6, 6, 6, 7, 8]
    x = 6

    # Find lower bound (first position where x can be inserted)
    lo = bisect.bisect_left(v, x)
    print(lo)

    # Find upper bound (first position where a value greater than x can be inserted)
    up = bisect.bisect_right(v, x)
    print(up)

if __name__ == "__main__":
    main()
