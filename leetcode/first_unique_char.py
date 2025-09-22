"""
First Unique Character in a String (LeetCode)

found at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1

This solution beats 7.87% of other submitted solutions
"""

# takes sorted string and find first unique element
def only_unique_chars(s):
    if len(s) > 1:
        i = 0
        # O(n^2)
        while i < len(s)-1:
            #print(i, i+1, ":", s[i], s[i+1], end=" ")
            if s[i] == s[i+1]:
                # O(n)
                a = "".join(c for c in s if c != s[i])
                s = a
            else:
                i += 1
            #print(s, "-->", i, i+1)
    return s

# O(nlogn) + O(n^2) = O[n(logn + n)]
def firstUniqChar(s: str) -> int:
    # find unique characters in s
    uniquechars = only_unique_chars("".join(sorted(s)))
    print(uniquechars)
    if not uniquechars:
        return -1
    # return first character that is both in s and in uniquechars
    for i in range(len(s)):
        if s[i] in uniquechars:
            return i
