"""
Problem Statement -> A rotated sorted array is an array of numbers in ascending order, in which a portion of the array
is moved from from the beginning to the end. Given a rotated sorted array of unique numbers, return the index of a 
target value. If the target value is not present return -1.

Example of rotated sorted array -
A possible rotation of [1,2,3,4,5] is [3,4,5,1,2] where the first two numbers are moved to the end.
"""
from typing import List

def find_the_target_in_a_rotated_sorted_array(nums: List[int], target:int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right)// 2

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return left if nums and nums[left] == target else -1

print(find_the_target_in_a_rotated_sorted_array([8,9,1,2,3,4,5,6,7], 1))