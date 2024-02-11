dict = {}
dict = {'a': 1, 'b': 2, 'c': 3}
print(dict['a']) # 1

# Add a Key-Value Pair
dict['d'] = 4

# Remove a Key-Value Pair
del dict['d']

# Check if a Key is in a Dictionary
print('a' in dict) # True

# Check if a Value is in a Dictionary
print(1 in dict.values()) # False

# Iterate Over a Dictionary with Items
for key, value in dict.items():
    print(key, value)
    # a 1
    # b 2
    # c 3


# Filter Dictionaries by Value with Dictionary Comprehension
filtered = {k: v for k, v in dict.items() if v > 1}
print(filtered) # {'b': 2, 'c': 3}

# Count Occurrences with Dictionary Comprehension
list = ['a', 'b', 'a', 'c', 'a', 'b', 'd']
frequency_dict = {x: list.count(x) for x in list}
print(frequency_dict) # {'a': 3, 'b': 2, 'c': 1, 'd': 1}

