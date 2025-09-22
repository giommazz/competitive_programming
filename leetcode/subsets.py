# Solving time: 41 minutes

# subsets.py
# Given an array nums of unique integers, return all possible subsets of nums.
# The solution set must not contain duplicate subsets. You may return the solution in any order.
# Neetcode: https://neetcode.io/problems/subsets?list=neetcode150
def subsets(nums: list[int]) -> list[list[int]]:
    """
    Generate all subsets (power set) of input list `nums`.

    Input:
    - `nums`: list of distinct integers (if duplicates exist, output may contain duplicates)

    Output:
    - `list[list[int]]`: list containing all subsets of `nums`

    Time complexity: O(n * 2^n), builds each subset by copying up to `n` elements
    Space complexity: O(n * 2^n), for storing all 2^n subsets, each of O(n) size; auxiliary O(2^n) to compute `nxt`

    Edge cases:
    - Empty input list `[]`
    - Presence of duplicate values in `nums`
    - Large `n` causing memory blowup
    """
    # Start with empty subset in `result`
    result = [[]]
    for x in nums:
        # Build new subsets `nxt` by appending `x` to each subset in `result`
        nxt = [s + [x] for s in result]
        # Append `nxt` to `result`
        result.extend(nxt)
    # Return all subsets in `result`
    return result