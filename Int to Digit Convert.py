# 1.........
def int_to_digits(n):
    return list(map(int, str(n)))

# Example usage
number = 12345
digits = int_to_digits(number)
print(digits)  # Output: [1, 2, 3, 4, 5]


# 2......
def int_to_digits(n):
    return [int(digit) for digit in str(n)]

# Example usage
number = 12345
digits = int_to_digits(number)
print(digits)  # Output: [1, 2, 3, 4, 5]


# 3.............
def IntToDigit(n):
    num=n
    while n:
        t=n%10
        n//=10
        if(t and num%t):
            return False
    return True
