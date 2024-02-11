# find num of 1 bits

class Solution:
    def hammingWeight(self, n:int) -> int:
        count = 0
        while n > 0:
            if n %2 != 0:
                count += 1
            n//=2
        return count


# print(Solution().hammingWeight(0b00000000000000000000000000001011))

class TestCase:
    def run():
        s = Solution()
        assert s.hammingWeight(0b00000000000000000000000000001011) == 3, "must be 3"
        assert s.hammingWeight(0b00000000000000000000000010000000) == 1, "must be 1"
        assert s.hammingWeight(0b11111111111111111111111111111101) == 31, "must be 31"



if __name__ == "__main__":
    TestCase.run()
    print("Every test case passed")