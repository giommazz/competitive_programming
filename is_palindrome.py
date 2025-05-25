# https://neetcode.io/problems/is-palindrome

def isPalindrome(s: str) -> bool:
    
    # transform all characters to lowercase
    s = s.lower()
    # filter out non-alphanumeric characters
    s = "".join([c for c in s if c.isalnum()])
    
    # length is 1, then True
    if len(s) == 1:
        return True
    
    start_idx, end_idx = 0, len(s)-1
    while start_idx < end_idx:
        if s[start_idx] != s[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1
    return True