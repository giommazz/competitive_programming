# container_with_most_water.py
# LeetCode: https://neetcode.io/problems/max-water-container?list=neetcode150

"""
Container With Most Water

You are given an integer array `heights` where `heights[i]` is the height of the i-th bar.
You may choose any two bars to form a container.
Return the maximum amount of water a container can store.
"""

from typing import List


def maxArea(heights: List[int]) -> int:
    """Return max water container area via two pointers.

    Input:
    - `heights`: List[int] of nonnegative heights, length >= 2

    Output:
    - int: max area between any two lines

    Time: O(n), single pass moving pointers inward
    Space: O(1), constant extra space for pointers and counters
    """

    def _rectangle(r: int, l: int, heights: List[int]) -> int:
        """Compute area formed by lines at indices `l` and `r`.

        Time: O(1)
        Space: O(1)
        """
        return (r - l) * min(heights[r], heights[l])

    # Initialize two pointers at widest possible container
    l, r = 0, len(heights) - 1
    result = 0

    # Shrink window from the side with smaller height and keep best area
    while l < r:
        # Compute current area and update running max
        result = max(_rectangle(r, l, heights), result)

        # Move pointer at smaller height *inward*
        # Basically: only way to improve is to improve "worst" (i.e., lowest) height 
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return result


# Example usage
heights1 = [1, 7, 2, 5, 4, 7, 3, 6]
heights2 = [1, 7, 1, 1, 1, 1, 2, 5, 12, 3, 500, 50, 7, 8, 4, 7, 38, 9, 10, 12, 6]
result = maxArea(heights2)
print(result)
