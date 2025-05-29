# Codility demo task

"""
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest integer > 0 not occurring in A.

- Given A = [1, 3, 6, 4, 1, 2], return 5
- Given A = [1, 2, 3], return 4
- Given A = [-1, -3], return 1

Assumptions:
- N is an integer within the range [1 ... 100,000];
- each element of array A is an integer within the range [-1000000 ... 1000000].
"""

def solution(A):
    # get set from A
    A_set = set(A)
    # transform it into list for easy access
    A_set = [e for e in A_set if e > 0]
    if not A_set: return 1
    sum_elements = 0
    sum_indices = 0
    for i in range(len(A_set)):
        sum_elements += A_set[i]    
        sum_indices += i + 1
        if sum_indices < sum_elements:
            return i+1
    return len(A_set)+1

    # Implement your solution here
    pass
