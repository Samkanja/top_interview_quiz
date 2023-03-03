def my_atoi(s:str) -> int:
    s = s.strip() 
    r = ''
    i = 0
    sign = 1
    
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        i += 1
        sign = -1
    num = 0
    while i < len(s):
        if not s[i].isnumeric():
            break
        else:
            num = num * 10 + int(s[i])
        i += 1
    num *= sign
    return -2**31 if num < -2**31 else 2**31 if num > 2**31 else num
 

f = '-91283472332'
print(my_atoi(f))