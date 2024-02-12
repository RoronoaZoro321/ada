def func(x):
    return (x * x) + x

def bsta(low,high,y):
    result =-1
    while low <= high:
        mid = (high + low)//2
        ans = func(mid)
        if ans <= y:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

def main():
    sumu = int(input())
    print(bsta(0,sumu,sumu))

main()
