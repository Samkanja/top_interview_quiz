def str_str(haystack:str, needle:str):
    if needle not in haystack or len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:
            return i
        
haystack = 'sadbutsad'
needle = 'sad'
print(str_str(haystack,needle))