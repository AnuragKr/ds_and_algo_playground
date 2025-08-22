"""
Problem Statement -> Given an array of integers sorted in non-decreasing order, return the first and last indexes of a 
                     target number. If the btarget is not found, return [-1,-1] 
"""
from typing import List

def first_and_last_occurence_of_a_number(nums:List[int], target:int) -> List[int]:
    lower_bound = lower_bound_binary_search(nums,target)
    upper_bound = upper_bound_binary_search(nums,target)
    return [lower_bound,upper_bound]

def lower_bound_binary_search(nums:List[int], target:int) -> int:
    left,right = 0,len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums and nums[left] == target else -1

def upper_bound_binary_search(nums:List[int], target:int) -> int:
    left,right = 0,len(nums)
    while left < right:
        mid = (left + right) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid
    return right if nums and nums[right] == target else -1

print(first_and_last_occurence_of_a_number([1,2,3,4,4,4,5,6,7,8,9,10,11],4))