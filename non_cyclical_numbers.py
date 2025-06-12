# non_cyclical_numbers.py

# Time complexity O(logn)
# Space complexity O(n)
def isHappy(self, n: int) -> bool:
    
    # initialize hashset 
    seen = set()
    # keep on running the loop until return False or true
    while True:
        # sum the squares
        squared = sum([int(i)**2 for i in str(n)])
        print(squared)
        # non-cyclical number
        if squared == 1:
            return True
        else:
            # searching and adding in a hash set has O(log n)
            if squared not in seen:
                seen.add(squared)
                # `squared` becomes the new `n` 
                n = squared
            else:
                return False