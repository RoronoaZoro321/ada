class TestCase:
    def run():
        s = Solution()
        assert s.hammingWeight(0b00000000000000000000000000001011) == 3, "must be 3"
        assert s.hammingWeight(0b00000000000000000000000010000000) == 1, "must be 1"
        assert s.hammingWeight(0b11111111111111111111111111111101) == 3, "must be 3"



if __name__ == "__main__":
    TestCase.run()
    print("Every test case passed")