# https://neetcode.io/problems/binary-search

def my_search(nums: list[int], target: int) -> int:
    return _binary_search(nums, 0, len(nums) - 1, target)

def _binary_search(nums: list[int], left: int, right: int, target: int) -> int:
    # Base case: empty sublist
    if left > right:
        return -1

    # find middle element
    mid = round((left + right) / 2)
    
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        # search left half
        return _binary_search(nums, left, mid - 1, target)
    else:
        # search right half
        return _binary_search(nums, mid + 1, right, target)
    
# solution from the website, not using recursion
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1