"""
Problem Statement -> Given an integer array, write a function which returns the sum of values between two indexes.
"""
from typing import List
def sum_range(nums: List[int], i: int, j: int) -> int:

    prefix_sum = [nums[0]]

    for idx in range(1,len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[idx])

    if i == 0:
        return prefix_sum[j]

    return prefix_sum[j] - prefix_sum[i-1]

print(sum_range([3,-7,6,0,-2,5],2,4))
