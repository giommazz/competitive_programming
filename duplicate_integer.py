# https://neetcode.io/problems/duplicate-integer
import time

# Sorting algorithm: time complexity O(nlogn), space complexity O(1)
def hasDuplicate_sorted(nums: list[int]) -> bool:
    nums = sorted(nums)
    if len(nums) == 1:
        return False
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Using hashtables via the set() structure: time complexity O(n), space complexity O(n)
def hasDuplicate_hashset(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)

nums=[1,2,3,1,2,3]
print(hasDuplicate_sorted(nums))
print(hasDuplicate_hashset(nums))
