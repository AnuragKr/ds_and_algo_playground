"""
Problem Statement -> Given an array of integers that are sorted in ascending order and a target value, we need to 
return the indexes of any pair of numbers in the array that sum to the target.
"""

def pair_sum_sorted(nums, target):
    """
    Finds the indices of a pair of numbers in a sorted array that sum to a target value.

    Args:
        nums (list[int]): A sorted list of integers.
        target (int): The target sum.

    Returns:
        list[int]: A list containing the indices of the two numbers, or an empty list if no such pair exists.

    Example:
        i/p -> array = [-5, -2, 3, 4, 6], target = 7
        o/p -> [2, 3]
    """
    left = 0
    right = len(nums) - 1

    # The core logic is to leverage the sorted array with two pointers.
    # We move the pointers towards the center until we find a match or they cross.
    while left < right:
        pair_sum = nums[left] + nums[right]
        if pair_sum < target:
            # Sum is too small, need a larger value.
            # Move the left pointer to the right.
            left += 1
        elif pair_sum > target:
            # Sum is too large, need a smaller value.
            # Move the right pointer to the left.
            right -= 1
        else:
            # Found the pair.
            return [left, right]
    
    # If the loop completes without finding a pair, return an empty list.
    return []

# The detailed breakdown of the principle.
"""
Underlying Principle -> Two Pointer Problem

1. Two Pointers: One at the start (smallest) and one at the end (largest).

2. Sum and Compare: 
   - If sum is too small, move left pointer right.
   - If sum is too large, move right pointer left.
   - If sum is equal, return the indices.

3. Narrow the Search: This process efficiently narrows the search space until a solution is found or the pointers cross.

Why it works:
This method is efficient because the sorted array allows us to make a directional decision at each step. 
By moving the pointers inwards, we are guaranteed to either find the solution or confirm that no solution exists in 
a single pass, resulting in an optimal O(n) time complexity.
"""