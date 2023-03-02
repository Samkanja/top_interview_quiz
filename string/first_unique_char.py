from collections import defaultdict


def first_uniq_char(s:str) -> int:
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]

   

    for val in d.values():
        if len(val) == 1:
            return val[0]
    return -1
s = 'loveleetcode'
print(first_uniq_char(s))
    