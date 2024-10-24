def solve():
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]

    count = 0

    for i in range(n):
        for j in range(n):
            if v[i][j] < 0:
                ap= abs(v[i][j])
                count += ap

                for k in range(n):
                    if i + k < n and j + k < n:
                        v[i + k][j + k] += ap

    print(count)


t = int(input())
for _ in range(t):
    solve()
