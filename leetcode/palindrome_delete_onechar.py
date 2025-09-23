# palindrome_delete_onechar.py
# https://leetcode.com/problems/valid-palindrome-ii/description/

"""
Given a string S consisting of lowercase English characters, determine if you can make it a palindrome by removing at most 1 character.

Examples:
- abca -> True  # abca -> aba
- caba -> True # caba -> aba
- racercar --> True (racecarby eliminating either 'e' or 'r', racrcar)
- abbab --> True
- abcd --> False
- btnnure --> False
"""


def is_palindrome(s):
    """
    Check if string `s` reads same forward/backward.

    Input:
    - s: str subject to palindrome check.

    Output:
    - bool: True when palindrome.

    Time complexity: O(n), compare each mirrored pair (extrema of string) once
    Space complexity: O(1), pointers only take constant space
    """
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def is_atMost_oneChar_palindrome(s):
    """
    Decide if removing <=1 char yields palindrome.

    Input:
    - s: str candidate for single-removal palindrome.

    Output:
    - bool: True when palindrome achievable.

    Time complexity: O(n), scan string once and reuse palindrome check *once*
    Space complexity: O(1), only indices stored.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Evaluate skipping one char on either side: execute only once because can delete only one character
            return is_palindrome(s[left + 1 : right + 1]) or is_palindrome(s[left:right])
        left += 1
        right -= 1
    return True