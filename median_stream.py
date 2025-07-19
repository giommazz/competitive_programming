# median_stream.py
"""
Implementation of two classes implementing the computation of the median on a list of integers.
The difference lies in how the add function, and related retrieval of the median, are computed:
    -   StreamMedian: using two different `add` functions, one based on sorting at each add, a more efficient one based on bisection
    -   StreamMedianHeaps: using a max-heap and a min-heap (with all elements larger than the ones in max-heap), and computing the median using heap roots
"""

import bisect
class StreamMedian():
    
    def __init__(self, nums=None):
        if nums:
            if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)): # check whether `nums` is sorted in O(n)
                self.nums = nums
            else: # `nums` is not sorted
                self.nums = sorted(nums)
        else: # constructor with empty list
            self.nums = []

    # two different implementations of addition: 1) sorting each time, 2) using `bisect`
    # Time complexity O(nlogn)
    def add_sort(self, new_elem: int):
        self.nums.append(new_elem)
        self.nums = sorted(self.nums) # order `nums`
    # Time complexity O(n)
    def add_bisect(self, new_elem: int):
        bisect.insort(self.nums, new_elem)
    
    # assumption: nums is always ordered
    # Time complexity O(1)
    def median(self):
        n = len(self.nums)
        if n == 0:
            raise ValueError("List is empty")
        
        mid_idx = n//2
        if n % 2 == 1: # odd case
            return self.nums[mid_idx]
        else: # even case
            hr = self.nums[mid_idx]
            hl = self.nums[mid_idx-1]
            return (hr + hl)*0.5

import heapq
class StreamMedianHeaps:
    def __init__(self, nums=None):
        # use a) "left" max-heap (`low`), b) "right" min-heap (`high`), to keep track of middle elements for computing median
        self.low = []   # max-heap via negation
        self.high = []  # min-heap
        if nums:
            for n in nums:
                self.add(n)
            
    # Properties enforces by add:
    #   -   every element in -`low` <= every element in `high`
    #   -   sizes of `low` and `high` differ at most by 1
    def add(self, new_elem):
        
        # 1) insert
        # `low` is empty or `new_elem` is bigger than `low`'s root (i.e., the largest element in the max-heap)
        if not self.low or new_elem <= -self.low[0]:
            heapq.heappush(self.low, -new_elem)
        else:
            heapq.heappush(self.high, new_elem)
        
        # 2) rebalance
        if len(self.low) > len(self.high)+1:
            # push largest element of `low` into `high`
            heapq.heappush(self.high, -heapq.heappop(self.low))
        # push smallest element of `high` into `low`
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    
    def median(self):
        if not self.low and not self.high:
            raise ValueError("List is empty")
        
        # odd case
        if len(self.low) > len(self.high):
            return -self.low[0]
        # even case
        return (-self.low[0] + self.high[0])*0.5


a = [2, 5, 10]
b = StreamMedianHeaps(a)
print(a)
print(f"{[-e for e in b.low]}\t{b.high}")
print(b.median())