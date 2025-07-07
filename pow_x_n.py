import sys
sys.set_int_max_str_digits(1000000) 

# helper function working only for positive `n`
# time complexity: O(logn), because each time we compute a product on *only half* of the `x`
# space complexity: also O(logn), since we need to store `p` as many times as we compute `myPow_(x, int(n/2))`
def myPow_(x: float, n: int) -> float:
    if n == 0: return 1
    if n == 1: return x
    if n == 2: return x*x
    if x == 0: return 0
    
    p = myPow_(x, int(n/2)) # compute product on *only half* of the `x`
    if n % 2 == 1: # n is odd
        return p*p*x # reuse info from previous computations
    else: # n is even
        return p*p
    
# if n > 0 then return `myPow_(x, n)`, else compute `1/myPow_(x, -n)`
def myPow(x: float, n: int) -> float:
    if n > 0: # final number is an integer
        return myPow_(x, n)
    else: # final number is a rational (fraction)
        denom = myPow_(x, -n)
        return 1/denom   

# myPow(2,1048576)
# myPow(2,33554432)
print(myPow(2,-3))
# myPow(2,1073741824)