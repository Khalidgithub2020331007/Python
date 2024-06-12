def remove_ith_character(s, i):
    # Ensure the index is within the bounds of the string
    if i < 0 or i >= len(s):
        raise ValueError("Index out of bounds")
    return s[:i] + s[i+1:]

# Example usage
string = "hello"
index = 1
new_string = remove_ith_character(string, index)
print(new_string)  # Output: "hllo"
