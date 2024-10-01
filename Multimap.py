# Create a multimap
multimap = {}

# Adding values to the multimap
multimap.setdefault('a', []).append(1)
multimap.setdefault('a', []).append(2)
multimap.setdefault('b', []).append(3)

print(multimap)  # Output: {'a': [1, 2], 'b': [3]}

# Accessing the values
print(multimap['a'])  # Output: [1, 2]


from collections import defaultdict

# Create a multimap
multimap = defaultdict(list)

# Adding values to the multimap
multimap['a'].append(1)
multimap['a'].append(2)
multimap['b'].append(3)

print(multimap)  # Output: {'a': [1, 2], 'b': [3]}

# Accessing the values
print(multimap['a'])  # Output: [1, 2]
