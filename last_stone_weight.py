# last_stone_weight.py
# https://neetcode.io/problems/last-stone-weight?list=blind75
import heapq

def lastStoneWeight(self, stones: list[int]) -> int:        
        # initialize max heap 
        maxheap = []
        # build `maxheap` as a negative min-heap: heaviest stone stored at `maxheap[0]`
        for stone in stones:
            heapq.heappush(maxheap, -stone)

        # while there are at least 2 stones in maaxheap
        while len(maxheap) > 1:

            # remove heaviest two stones from maxheap, and retrieve their weights 
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            
            # if same weight, they are both destroyed
            # if first is heaviest (remember all members of `maxheap` are now negative)
            if x < y:
                # ddd negative weight
                heapq.heappush(maxheap, x-y)
            if y < x:
                heapq.heappush(maxheap, y-x)
        
        if len(maxheap) == 0:
            return 0
        else:
            # remember: all elements of `maxheap` are negative
            return -maxheap[0]