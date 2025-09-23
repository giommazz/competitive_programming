# koko_eating_bananas.py
# Neetcode: https://neetcode.io/problems/eating-bananas?list=neetcode150

"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k.
Each hour, you may choose a pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
- Input: piles = [1,4,3,2], h = 9
- Output: 2
- Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
- Input: piles = [25,10,23,4], h = 4
- Output: 25

Constraints:
- 1 <= piles.length <= 1,000
- piles.length <= h <= 1,000,000
- 1 <= piles[i] <= 1,000,000,000"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find the minimum integer eating rate `k` so all bananas are eaten within `h` hours.

        Input:
        - `piles`: list of positive integers, the sizes of banana piles.
        - `h`: integer hours available to finish all piles.

        Output:
        - `int`: the minimal feasible eating rate `k`.

        Time complexity: O(n log M), where n = len(piles) and M = max(piles).
        Space complexity: O(1), excluding input storage.

        Edge cases:
        - Single pile
        - `h` equals number of piles
        - Large values in `piles`: left binary search
        - Trivial guard if `piles` is empty (constraints say n >= 1, but guard for robustness).
        """
        if not piles: # empty `piles`
            return 0 # Defensive solution: problem guarantees at least one pile.

        if len(piles) == 1: # single pile
            return ceil(piles[0]/h)
        
        if h == len(piles): # must eat at least 1 per hour, tight upper bound max(piles)
            return max(piles)
        
        # Helper: compute total hours needed to eat all bananas if eating `rate` = bananas/hour.
        def eating_time(rate: int) -> int:
            # One hour per chunk of `bananas` / `rate`
            return sum(ceil(bananas / rate) for bananas in piles)

        # Binary search on `k` over [1, max(piles)] (1 <= `k` <= max pile size).
        left, right = 1, max(piles)
        k = right # Initialize with largest possible feasible rate

        # Modified binary search: shrink toward minimal feasible rate.
        while left <= right: 
            mid = (left + right) // 2 # Candidate rate.
            eating_hours = eating_time(mid)

            # left binary search, even when `eating_hours == h` we keep looking left
            if eating_hours <= h: # Feasible rate
                # record, then try smaller rate (look left)
                k = min(mid, k)
                right = mid-1
            else: # Infeasible rate
                # Need a larger rate to use less hours
                left = mid+1

        return k