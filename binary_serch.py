def binarySearch(array, x, low, high):
    while low <= high:
        mid = (high + low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binarySearch(array, x, low, high):
    if high >= low:
        mid = (high + low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1
    
def binarySearch_closest_with_duplicate(array, x, low, high):
    closest_below = None
    closest_above = None
    while low <= high:
        mid = (high + low)//2
        if array[mid] == x:
            return (mid, mid)
        elif array[mid] < x:
            closest_below = mid
            low = mid + 1
        else:
            closest_above = mid
            high = mid - 1
    return (closest_below, closest_above)


# array = [3, 4, 7, 8, 10, 8, 9]
# x = 6
# result = binarySearch_closest_with_duplicate(array, x, 0, len(array)-1)
# print(result) # (2, 3)



# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4

# result = binarySearch(array, x, 0, len(array)-1)
# print(result) # 1


def binarySearch_last_occurrence(array, x, low, high):
    result = -1
    while low <= high:
        mid = (high + low)//2
        if array[mid] == x:
            result = mid
            low = mid + 1
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result

# a = [1, 2, 2, 2, 3, 4, 7, 8, 8, 8, 9, 10]
# x = 8
# result = binarySearch_last_occurrence(a, x, 0, len(a)-1)
# print(result) # 9

def f(x):
    return x**3 + 3*x+10

def binarySearch_Answer(low,high,ys):
    while low <= high:
        mid = (high + low)//2
        y = f(mid)
        if y == ys:
            return mid
        elif ys < y:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binarySearch_Answer(0,100,658774))

def bin_closest_epsilon(low, high, ys, epsilon):
    closest_below = None
    while low <= high:
        mid = round((high + low)//2)
        y = f(mid)
        if abs(y - ys) < epsilon:
            return mid
        elif ys < y:
            high = mid - epsilon
        else:
            closest_below = mid
            low = mid + epsilon
    return closest_below

print(bin_closest_epsilon(0,10,100, 0.01)) # 81