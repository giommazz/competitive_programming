# permutation_string.py
# Solving time: 1h05
# Neetcode: https://neetcode.io/problems/permutation-string?list=neetcode150
def checkInclusion(s1: str, s2: str) -> bool:
    """
    Determine whether `s2` contains a permutation of `s1` as a substring.

    Input:
    - `s1`: String with lowercase letters
    - `s2`: String with lowercase letters

    Output:
    - `bool`: `True` if `s2` contains permutation of `s1`, `False` otherwise

    Brute-force approach:
    - Enumerate all permutations of `s1` (count `n!` for `n = len(s1)`), then check membership in `s2`
    - Time: O(n! * m) where `m = len(s2)`; Space: O(n! * n) to hold permutations (or O(1) if generated on the fly)

    Current approach (my solution):
    - Scan `s2` and, when a character appears in `s1`, test the aligned length-`n` window using character counts
    - Time: O(m * n) in worst case, due to recomputing counts for each tested window; Space: O(n) for character counts

    Neetcode approach (Neetcode solution):
    - Maintain sliding-window counts for `s2` of length `n` and compare to counts of `s1`
    - Time: O(m + n); Space: O(1) with fixed alphabet size (26 lowercase letters)
    """
    def _are_anagrams(a, b):
        """
        Check whether `a` and `b` (same length) are anagrams (identical character counts).

        Input:
        - `a`: String with same length as `b`
        - `b`: String with same length as `a`

        Output:
        - `bool`: `True` if counts match, `False` otherwise
        """
        assert len(a) == len(b), "Strings must be of same length!"
        # Build counts for `a`
        tmp = {}
        for c in a:
            if c in tmp:
                tmp[c] += 1
            else:
                tmp[c] = 1
        # Decrease counts using `b`
        for c in b:
            if c in tmp:
                tmp[c] -= 1
                if tmp[c] == 0:
                    del tmp[c]
            else:
                return False
        return True

    if s1 and s2:
        n = len(s1)
        m = len(s2)
        # Scan `s2` and test candidate sliding windows of length `n`
        for i in range(len(s2)):
            if s2[i] in s1:
                if i + n <= m:
                    if _are_anagrams(s1, s2[i:i + n]):
                        return True
        return False


def checkInclusion_neetcode(s1: str, s2: str) -> bool:
    """
    Sliding-window optimal solution (NeetCode) using fixed-size counts of 26 letters.

    Input:
    - `s1`: String with lowercase letters
    - `s2`: String with lowercase letters

    Output:
    - `bool`: `True` if `s2` contains permutation of `s1`, `False` otherwise
    """
    # Guard against `s1` longer than `s2`
    if len(s1) > len(s2):
        return False

    # Allocate fixed-size counts for lowercase letters
    s1Count, s2Count = [0] * 26, [0] * 26
    # Fill initial counts for `s1` and first window in `s2`
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # Count how many letter positions currently match exactly
    matches = 0 # if `matches` gets to 26, all counts match and permutation exists
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    # Slide window [l, r) over `s2`: `r` starts from `len(s1)` and `l` moves with the window
    l = 0
    for r in range(len(s1), len(s2)):
        # Early exit when all letters match
        if matches == 26:
            return True

        # Expand window on right by including `s2[r]`
        index = ord(s2[r]) - ord('a') # index of letter in the alphabet in 0-25
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]: # if count of letter in `s1` and `s2` is the same, increase matches
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]: # if count of letter in `s1` > count of letter in `s2`, decrease matches
            matches -= 1

        # Shrink window on left by excluding `s2[l]`
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]: # if count of letter in `s1` and `s2` is the same, increase matches
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]: # if count of letter in `s1` < count of letter in `s2`, decrease matches
            matches -= 1
        l += 1

    # Check if last window in `s2` matches all letter counts in `s1` after loop ends
    return matches == 26