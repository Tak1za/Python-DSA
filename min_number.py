import time
import random

nums = [random.randrange(100) for x in range(100)]
print(nums)

def minNumN(nums):
    start = time.time()
    minNum = 99999999999999
    for i in range(len(nums)):
        if nums[i] < minNum:
            minNum = nums[i]
    end = time.time()
    return minNum, end-start

print ("Minimum number is %d and it took %10.7f seconds" % minNumN(nums))