def reverse_interger(x:int) -> int:
    s = str(x)
    res = ''
    for i in s:
        if i.isnumeric() and i != '0':
            res = i + res

        
        

    return int(-res)

s = -120
print(reverse_interger(s))