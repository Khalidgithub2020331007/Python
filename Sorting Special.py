for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # print(_ + 1)
    c = []
    for i in range(n):
        if a[i] % k == 0:
            a[i] = k
        else:
            a[i] = a[i] % k
        c.append(i + 1)
    #
    # print(a)
    # print(c)

    zipped = list(zip(a, c))  # Convert zip object to a list
    zipped.sort(key=lambda x: x[0], reverse=True)  # Correct the typo and sort the list

    nb = [x for _, x in zipped]

    for i in nb:
        print(i, end=' ')
    print()
