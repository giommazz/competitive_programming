"""
Maximum Subarray

Given an array of integers nums, find the subarray with the largest sum and return the sum.
A subarray is a contiguous non-empty sequence of elements within an array.

https://neetcode.io/problems/maximum-subarray?list=neetcode150

Three implementations: 
- quadratic rolling-sum baseline
- Kadane-style variant
- the canonical Kadane

Intuition of why Kadane works:
- A negative running prefix can never help a future subarray -> discard it
- Track best sum seen so far while scanning once.
- Initialize with the first value to handle the all-negative case correctly.
"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
    """Brute-force baseline with rolling sum.

    Input:
    - nums: non-empty list of ints

    Output:
    - max contiguous subarray sum

    Time: O(n^2): two nested scans per start index
    Space: O(1): constant counters only
    """
    if nums:
        maxsum = nums[0]
        for i in range(len(nums)):
            currsum = nums[i]
            maxsum = max(maxsum, currsum)
            for j in range(i+1, len(nums)):
                currsum += nums[j]
                maxsum = max(maxsum, currsum)
        return maxsum

def maxSubArray(nums: List[int]) -> int:
    """Kadane variant: restart when prefix harmful.

    Input:
    - nums: non-empty list of ints

    Output:
    - max contiguous subarray sum

    Time: O(n): single left-to-right pass
    Space: O(1): constant memory (currsum, maxsum, i)
    """
    if nums:
        maxsum = nums[0]
        currsum = nums[0]
        i = 1
        while i < len(nums):
            # restart if negative prefix and fresh start preferred
            if currsum < 0 and (nums[i] >= 0 or nums[i] > currsum):
                currsum = nums[i]
            else:
                currsum += nums[i]
            maxsum = max(currsum, maxsum)
            i += 1
        return maxsum

def maxSubArray(nums: List[int]) -> int:
    """Standard Kadane

    Input:
    - nums: non-empty list of ints

    Output:
    - max contiguous subarray sum

    Time and space complexity as above Kadane variant
    """
    if nums:
        maxsum = nums[0]
        currsum = nums[0]
        i = 1
        while i < len(nums):
            if currsum < 0:
                currsum = 0 # drop negative prefix, restart at i (simpler than above Kadane variant)
            currsum += nums[i]
            maxsum = max(currsum, maxsum)
            i += 1
        return maxsum
