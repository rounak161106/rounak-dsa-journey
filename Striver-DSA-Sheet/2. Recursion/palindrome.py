def palindrome(s):
    if (len(s)==1 or len(s) == 2) and s[0] == s[-1]:
        return True
    elif s[0] != s[-1]:
        return False
    return palindrome(s[1:len(s)-1])

print(palindrome("a"))