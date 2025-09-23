# k_most_frequent.py
# https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

"""
Given a non-empty array of integers, return up to K most frequent elements, in the order of descending frequency.
You may assume k is always valid, 1 <= k <= number of unique elements.

For example,
- Given [1, 1, 1, 2, 2, 3] and k = 2,  return [1, 2].
- Given [1, 1, 1, 1] and k = 1 return [1].
- Given [1, 2, 3, 2, 3] and k = 2 return [2 , 3].
- Given [1, 2, 3, 4] and k = 2 return [1, 2]
"""


import heapq


def _browseArray(nums):
    """
    Build frequency map keyed by string form.

    Input:
    - nums: list of ints subject to counting.

    Output:
    - dict: map from str value to occurrence count.

    Time complexity: O(n); single pass touches each value once.
    Space complexity: O(m); store one entry per unique value, with m distinct values.
    """
    frequencies = dict()
    for elem in nums:
        if str(elem) in frequencies.keys():
            frequencies[str(elem)] += 1
        else:
            frequencies[str(elem)] = 1
    return frequencies


def _createHeap(frequencies):
    """
    Build max-heap representing counts.

    Input:
    - frequencies: dict mapping str value to count.

    Output:
    - list: heap of (-count, key) pairs.

    Time complexity: O(m log m), with m the number of distinct elements, to push each entry into heap.
    Space complexity: O(m), as heap stores all entries.
    """
    hFreq = []
    for key, value in frequencies.items():
        heapq.heappush(hFreq, (-value, key)) # use negative counts to simulate max-heap
    return hFreq


def topKFrequent(nums, K):
    """
    Fetch K most frequent values via heap selection.

    Input:
    - nums: list of ints to analyze.
    - K: count of top frequencies requested.

    Output:
    - list: stringified values sorted by descending frequency.

    Time complexity: O(n) + O(m log m) + O(K log m), to build counts then perform heap operations
    Space complexity: O(m), to build frequency map, then heap
    """
    frequencies = _browseArray(nums)
    print(frequencies)
    hFreq = _createHeap(frequencies)
    print(hFreq)
    result = []

    for _ in range(0, K):
        result.append(heapq.heappop(hFreq)[1]) # pop next most frequent value

    return result

# nums, K = [1, 1, 1, 2, 2, 3], 2
# nums, K = [1, 1, 1, 1], 1
# nums, K = [1, 2, 3, 2, 3], 2
nums, K = [1, 2, 3, 4], 2
print(topKFrequent(nums, K))
