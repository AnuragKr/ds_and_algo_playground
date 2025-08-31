"""
Problem Statement -> Given an array of integers, return the indexes of any two numbers that add up to a target.
If no pair found , returns an empty array.
"""
from typing import  List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], idx]
        hashmap[num] = idx
    return []