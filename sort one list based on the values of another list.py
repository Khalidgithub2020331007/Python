# Define the lists
list1 = [3, 1, 2]
list2 = ['apple', 'banana', 'cherry']

# Zip the lists together
zipped_lists = zip(list1, list2)

# Sort the zipped list based on the first list
sorted_zipped_lists = sorted(zipped_lists)

# Extract the sorted second list
sorted_list2 = [element for _, element in sorted_zipped_lists]

print(sorted_list2)
