a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find the Index of an Element in List
idx = a.index(2) # 1

# Slice a List
sliced = a[2:5] # [3, 4, 5]
slice_from_end = a[-3:] # [8, 9, 10]

# Check if an Element is in a List
print(2 in a) # True

# Count the Occurrences of an Element in a List
print(a.count(2)) # 1

# Add an Element to the End of a List
a.append(11)

# Add an Element at a Specific Index
a.insert(0, 0)

# Remove an Element by Value
a.remove(0)

# Remove an Element by Index
a.pop(0)

# Remove the Last Element
a.pop()

# Remove All Elements
# a.clear()

# Copy a List
b = a.copy()

# Concatenate Lists
c = a + b

# Merge Lists without Duplicates
merged = list(set(a + b))
merged.sort()
print(merged) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Repeat a List
a = [1, 2]
d = a * 3 # [1, 2, 1, 2, 1, 2]

# Iterate Over a List
for i in a:
    print(i)

# Iterate Over a List with an Index
for index, value in enumerate(a):
    print(index, value)
    # 0 1
    # 1 2

# Checking if Any Element Satisfies a Condition
# any_satisfy = any(condition(x) for x in original_list) 
print(any(x > 5 for x in a)) # False

# all_satisfy = all(condition(x) for x in original_list)
print(all(x >= 1 for x in a)) # True

max_value = max(a)
min_value = min(a)
sum_value = sum(a)

# List Comprehension
# [expression for item in iterable if condition]
original_list  = [4, 5, 6, 7]
squared = [x**2 for x in original_list if x > 5] # [36, 49]
l = [i for i in range(1,3)] # [1, 2]