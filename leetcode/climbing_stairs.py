# climbing_stairs.py

# recursive solution 
# Time complexity O(2^n). You can see this drawing a tree: you start at a node `n` then, for each
#       node, the subtrees rooted in its children will explore stair-climbing with `n-1` and `n-2`.
#       The tree has height `n` --> O(2^n) complexity
# space complexity O(1)
def climbStairs_recursion(n: int) -> int:
    if n <= 2:
        return n
    else:
        return climbStairs_recursion(n-1) + climbStairs_recursion(n-2)
    
# linear solution: based on the observation that s(n) = s(n-1) + s(n-2)
# time complexity O(n), space complexity O(1)
def climbStairs_linear(n: int) -> int:
    if n <= 2:
        return n
    else:
        past1, past2 = 1, 2
        for i in range(3, n+1):
            ways_to_climb_stairs = past1 + past2
            past1 = past2
            past2 = ways_to_climb_stairs
        return ways_to_climb_stairs
    
# Remark: since this is the Fibonacci sequence, one can also use the Golden Ratio formula to 
#       solve the exercise: https://en.wikipedia.org/wiki/Fibonacci_sequence