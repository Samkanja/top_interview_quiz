from typing import List

def two_sum(nums:List[int],target:int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return [i,d[target - nums[i]]]
        d[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))