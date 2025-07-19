# last_stone_weight.py
# https://neetcode.io/problems/last-stone-weight?list=blind75
"""
You are given an array of integers `stones` where `stones[i]` represents the weight of the i-th stone.

You want to run a simulation on the stones as follows:
-   At each step, you choose the two heaviest stones, with weight x and y and smash them together
        -   If x == y, both stones are destroyed
        -   If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.
Return the weight of the last remaining stone or return 0 if none remain.


Example 1
    Input: stones = [2,3,6,2,4]
    Output: 1
    
    Explanation:
        We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
        We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
        We smash 2 and 2, so the array becomes [1].

Example 2:
    Input: stones = [1,2]
    Output: 1


"""


import heapq

def lastStoneWeight(self, stones: list[int]) -> int:        
        # initialize max heap 
        maxheap = []
        # build `maxheap` as a negative min-heap: heaviest stone stored at `maxheap[0]`
        for stone in stones:
            heapq.heappush(maxheap, -stone)

        # while there are at least 2 stones in maxheap
        while len(maxheap) > 1:

            # remove heaviest two stones from maxheap, and retrieve their weights 
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            
            # if same weight, they are both destroyed
            # if first is heaviest (remember all members of `maxheap` are now negative)
            if x < y:
                # add negative weight
                heapq.heappush(maxheap, x-y)
            if y < x:
                heapq.heappush(maxheap, y-x)
        
        if len(maxheap) == 0:
            return 0
        else:
            # remember: all elements of `maxheap` are negative
            return -maxheap[0]