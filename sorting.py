a = [9,4,6,1,1]

# sort a list
a.sort() # [1,1, 4, 6, 9]
print(a)

# sort a list in reverse
a.sort(reverse=True) # [9, 6, 4, 1, 1]

# reverse a list
a.reverse() # [1, 1, 6, 4, 9]

# sort a list without modifying the original list
sorted_a = sorted(a)

# Removing Duplicates
unique = set(a)
unique = list(unique)
print(unique) # [9, 4, 6, 1]


d = {'a': 3, 'b': 1, 'c': 2}
# Sorting a dict by value
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=False)
print(sorted_d) # [('b', 1), ('c', 2), ('a', 3)]

# sort a class
# people = [Person('John', 30), Person('Jane', 25), Person('Dave', 40)]
# sorted_people = sorted(people, key=lambda x: x.age)


# sort list string
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz']
print(sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
# sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']
def MyFn(s):
    return s[-1]
print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']
