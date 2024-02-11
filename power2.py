# def isPowerOfTwo(n: int) -> bool:
#     return (n & n-1) == 0


# print(isPowerOfTwo(1))
# print(isPowerOfTwo(16))
# print(isPowerOfTwo(3))



# def isPowerOfFour(n: int) -> bool:
#     print(n)
#     if n == 1: return True
#     elif (n % 2) != 0: return False
#     elif n <1: return False
#     else: return isPowerOfFour(n/4)


# print(isPowerOfFour(16))



class Solution:
    def __init__(self):
        self.memo = {}
            
    def fib(self, n: int) -> int:
    
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            return self.memo[n]
		

s = Solution()
print(s.fib(3))