def sieve_of_eratosthenes(n):
    # Initialize a list of boolean values where True means the number is prime
    primes = [True] * (n + 1)  
    p = 2  # Start with the first prime number, 2
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    # Mark multiples of each prime starting from p
    while p * p <= n:
        if primes[p]:
            # Mark all multiples of p as False (not prime)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    # Collect and return all primes
    return [p for p in range(n + 1) if primes[p]]

# Example: Find all primes up to 50
print(sieve_of_eratosthenes(50))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
