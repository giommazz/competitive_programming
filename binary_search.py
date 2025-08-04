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
    

# returning leftmost found element
def binarysearch_left(nums, elem):
    n = len(nums)
    if n == 1:
        return 0
    
    mid = (n-1) // 2 

    if elem <= nums[mid]:
        # look left: nums[0] ... nums[mid-1]
        return binarysearch_left(nums[:mid+1], elem)
    else:
        # look right: nums[mid] ... nums[n]
        return mid + 1 + binarysearch_left(nums[mid+1:], elem)


 # Two other solutions of mine: leftmost and rightmost binary search
# returning rightmost found element
def binarysearch_right(nums, elem):
    n = len(nums)
    if n == 1:
        return 0
    
    mid = n // 2 

    if elem < nums[mid]:
        # look left: nums[0] ... nums[mid-1]
        return binarysearch_right(nums[:mid], elem)
    else:
        # look right: nums[mid] ... nums[n]
        return mid + binarysearch_right(nums[mid:], elem)

# solution from the neetcode, not using recursion
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