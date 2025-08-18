"""
Problem Statement -> Given a string, determine if it's a palindrome after removing all non-alphanumeric characters.
                     A character is alphanumeric if it's either a letter or a number.

i/p -> s = "racecar"
o/p -> True

i/p -> s = "abc123"
o/p -> False
"""

"""
Underlying Principle -> Two Pointer Problem
"""

def is_palindrome_valid(s: str) -> bool:
    left , right = 0, len(s)-1
    while left < right:
        #skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        #skip non-alphanumeric character from the right
        while left < right and not s[right].isalnum():
            right -= 1
        #if the characters at the left and right doesn't match then string is not a palindrome
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True