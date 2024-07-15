# Initialize an empty set
dynamic_set = set()

# Loop to get user input
while True:
    element = input("Enter an element to add to the set (or 'done' to finish): ")
    if element.lower() == 'done':
        break
    dynamic_set.add(element)

print("Final set:", dynamic_set)
