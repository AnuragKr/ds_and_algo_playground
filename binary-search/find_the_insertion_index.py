"""
Problem Statement -> Given a sorted array that contains unique values, along with an integer target.
                     1. If the array contains the target value, return its index.
                     2. Return the insertion index

What is insertion index ?
This is the index where the target would be if it were inserted in order, maintaining the sorted sequence of the array.
"""
from typing import List

def find_the_insertion_index(nums: List[int], target:int) -> int:
    left,right = 0,len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

print(find_the_insertion_index([1,2,3,4,5,7,8,9], 6))