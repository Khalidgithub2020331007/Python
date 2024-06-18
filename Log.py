import math

# Function to compute log base x of n
def log_base_x(n, x):
    return math.log(n, x)

# Example usage
n = 100
x = 10
result = log_base_x(n, x)
print(f"log base {x} of {n} is {result}")
