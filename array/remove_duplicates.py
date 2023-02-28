from typing import List

def remove_duplicates(nums:List[int]) -> int:
    l = 0
    for i in range(1,len(nums)):
        if nums[i - 1] == nums[i]:
            nums[l] = nums[i]

    return l

