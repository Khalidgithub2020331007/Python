def int_to_digits(n):
    return list(map(int, str(n)))

# Example usage
number = 12345
digits = int_to_digits(number)
print(digits)  # Output: [1, 2, 3, 4, 5]
