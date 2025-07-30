"""
Problem Statement -> Given an array of integers that are sorted in ascending order and a target value, we need to 
return the indexes of any pair of numbers in the array that sum to the target.

i/p -> array = [-5,-2,3,4,6], target = 7
o/p -> [2,3]
"""

"""
Pattern -> Two Pointer Problem

The core idea is to use two pointers, one starting at the beginning and the other at the end of the sorted array.
By summing the values at these pointers and comparing it to the target, we can decide whether to move the 
left pointer forward (if the sum is too small) or the right pointer backward (if the sum is too large), 
effectively narrowing down the search space until the target sum is found or the pointers cross.
"""

def pair_sum_sorted(nums,target):
    left = 0
    right = len(nums) - 1

    while left < right:
        pair_sum = nums[left] + nums[right]
        if  pair_sum < target:
            left += 1
        elif pair_sum > target:
            right -= 1
        else:
            return [left,right]
    
    return []