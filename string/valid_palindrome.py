def is_palindrome(s:str) -> bool:
    r = ''
    for x in s:
        if x.isalnum():
            r += x.lower()

    return r == r[::-1]
s = "0P"
print(is_palindrome(s))