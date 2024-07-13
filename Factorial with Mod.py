def factorial(n):
    if n == 0:
        return 1
    else:
        return (n%mod * factorial(n - 1)%mod)%mod

# Calling the function
n,mod=map(int,input().split())
result = factorial(n,mod)
print(result)  # Output: 120
