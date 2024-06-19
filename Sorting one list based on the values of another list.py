def sort_lists_based_on_first_list(list1, list2):
    # Zip the lists together
    zipped_lists = zip(list1, list2)
    
    # Sort the zipped list based on the first list
    sorted_zipped_lists = sorted(zipped_lists)
    
    # Extract the sorted lists
    sorted_list1 = [element for element, _ in sorted_zipped_lists]
    sorted_list2 = [element for _, element in sorted_zipped_lists]
    
    return sorted_list1, sorted_list2

# Example usage
list1 = [3, 1, 2]
list2 = ['apple', 'banana', 'cherry']
sorted_list1, sorted_list2 = sort_lists_based_on_first_list(list1, list2)
print(sorted_list1)  # Output: [1, 2, 3]
print(sorted_list2)  # Output: ['banana', 'cherry', 'apple']
