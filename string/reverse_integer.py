def reverse_interger(x:int) -> int:
    s = str(x)
    res = ''
    if s[0] == '-':
        sign = -1
    else:
        sign = 1
    for x in s:
        if x.isnumeric():
            res = x + res
    
    return int(res) * sign if -2**31 < int(res) < 2**31 else 0
   

s = -120
print(reverse_interger(s))