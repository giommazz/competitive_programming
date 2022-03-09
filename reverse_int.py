"""
Reverse Integer
found at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

import ctypes

class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            s = int("-" + str(x)[1:][::-1])
        else:
            s = int(str(x)[::-1])
        if s >= -2**31 and s <= 2**31 - 1:
            return ctypes.c_long(s).value
        else:
            return 0
