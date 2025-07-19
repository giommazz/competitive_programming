# https://neetcode.io/problems/single-number?list=neetcode150

# Time complexity: O(n)
# Space complexity: O(n)
def singleNumber_hashset(nums: list[int]) -> int:
    a = sum(nums)
    b = 2*sum(set(nums))
    return b-a

# Neetcode solution
# Time complexity: O(n)
# Space complexity: O(1)
# based on XOR bitwise operation, with properties:
#   -   (a XOR a) = 0   (1)
#   -   (a XOR 0) = a   (2)
def singleNumber(nums: list[int]) -> int:
    res = 0
    for num in nums:
        # XOR each element of the list with res
        # due to (1)-(2), pairs of identical numbers cancel out, leaving only unique element
        res = num ^ res 
    return res

