# binary_search.py
# https://neetcode.io/problems/binary-search

from math import ceil
def my_search(nums: list[int], target: int) -> int:
    """
    Binary search wrapper that returns index of target in sorted list, or -1 if not found.
    Uses `_binary_search()` as internal helper

    Inputs:
    - nums: sorted ascending list of ints
    - target: int to find

    Outputs:
    - index: int index of target, or -1 if not found

    Complexity:
    - Time: O(log n): halve search space each step.
    - Space: O(log n): recursion depth from halving.
    """
    return _binary_search(nums, 0, len(nums) - 1, target)

def _binary_search(nums: list[int], left: int, right: int, target: int) -> int:
    """
    Recursive binary search on subarray [left, right] (internal helper)

    Inputs:
    - nums: sorted ascending list of ints
    - left: start index (inclusive)
    - right: end index (inclusive)
    - target: int to find

    Outputs:
    - index: int index of target, or -1 if not found

    Complexity:
    - Time: O(log n): halve range each call.
    - Space: O(log n): call stack from halving.
    """
    # base case: empty range
    if left > right:
        return -1

    mid = round((left + right) / 2)
    
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return _binary_search(nums, left, mid - 1, target) # look on the right of `mid`
    else:
        return _binary_search(nums, mid + 1, right, target) # look on the left of `mid`

def binarysearch_right(nums, x):
    """
    Binary search that returns rightmost index of x in sorted list, or -1 if not fonud.

    Inputs:
    - nums: sorted ascending list of ints (may contain duplicates)
    - x: int value to locate

    Outputs:
    - index: int index of rightmost occurrence, or -1 if absent

    Complexity:
    - Time: O(log n): loop halves search region.
    - Space: O(1).

    Remark: to get binarysearch_left, change only one line 
        "left = mid+1"
    under equality branch
        into 
        "right = mid-1".
    """
    left, right = 0, len(nums)-1
    result = -1
    while left <= right:
        mid = ceil((left + right) / 2)
        if nums[mid] == x:
            result = mid # update result
            left = mid+1 # look on the right of `mid`
        elif nums[mid] > x:
            right = mid-1 # look on the left of `mid`
        else:
            left = mid+1 # look on the right of `mid`
    return result
