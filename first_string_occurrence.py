"""
Find the index of the first occurrence in a string

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
  Input: haystack = "sadbutsad", needle = "sad"
  Output: 0
  Explanation: "sad" occurs at index 0 and 6.
  The first occurrence is at index 0, so we return 0.

Example 2:
  Input: haystack = "leetcode", needle = "leeto"
  Output: -1
  Explanation: "leeto" did not occur in "leetcode", so we return -1. 
"""
# Beats 3.26%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx_h = 0
        first_idx = -1
        len_n = len(needle)
        len_h = len(haystack)
        if len_n > len_h:
            return -1
        while idx_h <= (len_h-len_n):
            test_h = haystack[idx_h:idx_h+len_n]
            if test_h == needle:
                return idx_h
            else: 
                idx_h += 1
        return -1
