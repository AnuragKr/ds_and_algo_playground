"""
Problem Statement -> Given a string, determine if it's a palindrome after removing all non-alphanumeric characters.
                     A character is alphanumeric if it's either a letter or a number.
"""

def is_palindrome_valid(s: str) -> bool:
    """
    Checks if a string is a palindrome after filtering out non-alphanumeric characters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Example:
        i/p -> s = "racecar"
        o/p -> True

        i/p -> s = "abc123"
        o/p -> False
    """
    left, right = 0, len(s) - 1
    
    # The core logic is to use two pointers to compare characters from both ends.
    # We skip any non-alphanumeric characters and check for a match.
    while left < right:
        # Skip non-alphanumeric characters from the left.
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from the right.
        while left < right and not s[right].isalnum():
            right -= 1
        
        # If the characters at the left and right don't match, the string isn't a palindrome.
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True

# A detailed breakdown of the principle.
"""
Underlying Principle -> Two Pointer Problem

1. Two Pointers: One at the start (left) and one at the end (right).

2. Filter and Compare:
   - We move the left pointer to the right until it points to an alphanumeric character.
   - We move the right pointer to the left until it points to an alphanumeric character.
   - If the characters at these pointers, converted to lowercase, don't match, it's not a palindrome.

3. Narrow the Search: This process efficiently narrows the search space from both ends, skipping irrelevant characters 
and checking for a match until the pointers cross.

Why it works:
This method is efficient because it avoids creating a new, filtered string. By using two pointers and skipping 
non-alphanumeric characters in-place, we can solve the problem with an optimal O(n) time complexity and O(1) space 
complexity.
"""