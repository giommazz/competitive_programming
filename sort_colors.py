# sort_colors.py
# Solving time: 40'
# LeetCode: https://leetcode.com/problems/sort-colors/description/

"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

def swap(nums, i, j):
    """
    Swap elements at indices `i` and `j` in `nums`.
    
    Input:
    - `nums`: List to modify
    - `i`: First index
    - `j`: Second index
    
    Output:
    - None (modifies `nums` in-place)
    """
    nums[i], nums[j] = nums[j], nums[i]

def browse(nums, start, end):
    """
    Find index of first number != 1 in `nums[start:end]`.
    
    Input:
    - `nums`: List to search
    - `start`: Starting index (inclusive)
    - `end`: Ending index (exclusive)
    
    Output:
    - `int`: Index of first non-1 element, or -1 if all are 1s
    """
    for i in range(start, end):
        if nums[i] != 1:
            return i
    return -1

def sort_colors(nums):
    """
    Sort array of colors (0=red, 1=white, 2=blue) in-place using two-pointer approach.
    
    Input:
    - `nums`: List of integers containing only 0, 1, and 2
    
    Output:
    - None (modifies `nums` in-place)
    
    Time complexity: O(n) - each element examined at most once across all `browse()` calls
    Space complexity: O(1) - only uses constant extra space for pointers
    """
    i, j = 0, len(nums) - 1  # i=left pointer, j=right pointer
    k = i + 1  # Track last searched position to avoid re-scanning
    
    while i < j:
        if nums[i] == 2:
            # Move 2s to the right end
            swap(nums, i, j)
            j -= 1
        elif nums[i] == 0:
            # 0s are already in correct position, move left pointer
            i += 1
            k = max(k, i + 1)  # Update `k` to avoid re-scanning
        else:  # nums[i] == 1
            # Find next non-1 element to swap with this 1
            # KEY OPTIMIZATION: Start search from `k` (not `i+1`) to avoid re-scanning
            #  -> this ensures each element is examined at most once across all browse() calls (linear complexity)
            k = browse(nums, k, j + 1)
            if k >= 0:
                swap(nums, i, k)
                k += 1  # Move k past the swapped element
            else:
                # All remaining elements are 1s, we're done
                return
