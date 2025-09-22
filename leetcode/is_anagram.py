# https://neetcode.io/problems/is-anagram

# hashtable (dict): time complexity O(n+m), space complexity O(n+m) 
def isAnagram(s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s1_dict, s2_dict = {}, {}
        for i in range(len(s1)):
            if s1[i] in s1_dict:
                s1_dict[s1[i]] += 1
            else:
                s1_dict[s1[i]] = 1
            if s2[i] in s2_dict:
                s2_dict[s2[i]] += 1
            else:
                s2_dict[s2[i]] = 1
        return s1_dict == s2_dict

# the solution provided on the website is even more elegant for incrementing the counters
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        # `countS.get(element)` returns `countS[element]` if the element is in `countS`, and 0 otherwise.
        # By default, `dict.get()` would return a NoneType object
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT