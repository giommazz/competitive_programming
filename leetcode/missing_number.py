# https://neetcode.io/problems/missing-number?list=neetcode150

"""
You are given an array nums containing n integers in the range [0, n] without any duplicates.
Return the single number in the range that is missing from nums.
Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
# Time complexity: O(n) for the summation
# Space complexity: O(1) for the memory storage
def missingNumber(nums: list[int]) -> int:
    sumnums = sum(nums) # sum all elements of `nums`
    n = len(nums)
    series_sum = int((n*(n+1))/2) # sum_{i in [n]} i
    return series_sum - sumnums