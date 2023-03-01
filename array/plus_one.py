from typing import List

def plus_one(digits:List[int]) -> List[int]:
    d_str = ''.join([str(i) for i in digits])
    num = int(d_str) + 1
    l = []
    while num > 0:
        l.append(num%10)
        num = num  // 10
    l = l[::-1]
    return l

digits = [4,3,2,1]
print(plus_one(digits))