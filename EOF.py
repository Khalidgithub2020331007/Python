import math

def r(n, k, ma):
    if n <= k:
        return 1
    if n in ma:
        return ma[n]
    if n % 2:
        ma[n] = r(n // 2, k, ma) + r(math.ceil(n / 2), k, ma)
        return ma[n]
    else:
        ma[n] = r(n // 2, k, ma) * 2
        return ma[n]

import sys

for s in sys.stdin:
    s = s.strip()
    if not s:
        break
    try:
        a, b = map(int, s.split())
        ans = r(a, b, {})
        print(ans)
    except ValueError:
        break
