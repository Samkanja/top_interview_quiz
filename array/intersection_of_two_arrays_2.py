from typing import List
def intersect(nums1:List[int],nums2:List[int]) -> List[int]:
    l = []
    for x in min(nums2,nums1):
        if x in max(nums2,nums1):
            l.append(x)

    return l


nums1 = [1,2,2,1]
nums2 = [2]
print(intersect(nums1,nums2)) 