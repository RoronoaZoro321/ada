# pip install -U memory_profiler
from memory_profiler import profile
 
@profile

def majorityElement(nums) -> int:
    temp = {}
    for i in nums:
        if i in temp:
            temp[i] += 1                
        else: 
            temp[i] = 1

    highest = 0
    index = 0
    for i in temp:
        if temp[i] > highest:
            highest = temp[i]
            index = i
    return index
 
if __name__ == '__main__':
    majorityElement([3,2,3])