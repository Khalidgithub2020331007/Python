a = [10, 20, 30, 40, 50]

# Find the index of the value 30
index = a.index(30)
print(index)  # Output: 2

# Find the index of the value 50
index = a.index(50)
print(index)  # Output: 4

# Attempting to find the index of a value not in the list
index = a.index(100)  # This will raise a ValueError
