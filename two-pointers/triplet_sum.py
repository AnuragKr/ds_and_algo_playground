"""
Problem Statement -> Given an array of integers, return all unique triplets `[a, b, c]` such that their sum equals zero.

If no such triplets are found, return an empty array.
"""
from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in an array that sum to zero.

    Args:
        nums (List[int]): An array of integers.

    Returns:
        List[List[int]]: A list of unique triplets, or an empty list if none are found.

    Example:
        i/p -> nums = [0, -1, 2, -3, 1]
        o/p -> [[-3, 1, 2], [-1, 0, 1]]
    """
    nums.sort()
    result = []
    
    # Iterate through the array with a single pointer.
    for idx in range(len(nums) - 2):
        # Optimization: If the first number is positive, we can stop.
        # Since the array is sorted, the sum of three positive numbers can't be zero.
        if nums[idx] > 0:
            break
        
        # Skip duplicate values for the first number to avoid duplicate triplets.
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue
            
        # Use a two-pointer approach on the rest of the array.
        left, right = idx + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[idx] + nums[left] + nums[right]
            
            if current_sum < 0:
                # Sum is too small, move the left pointer to increase the value.
                left += 1
            elif current_sum > 0:
                # Sum is too large, move the right pointer to decrease the value.
                right -= 1
            else:
                # Found a triplet that sums to zero.
                result.append([nums[idx], nums[left], nums[right]])
                
                # Move pointers and skip duplicate values for the second and third numbers.
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
    return result

# A detailed breakdown of the principle.
"""
Underlying Principle -> Two Pointer Problem

1. Sort the Array: Sorting the array is the key first step. It allows us to use the Two-Pointer approach efficiently 
and to easily handle duplicate triplets.

2. Three Pointers, One Fixed: We iterate through the array with one pointer (`idx`). For each `idx`, 
we treat `nums[idx]` as the first number of a potential triplet. We then use two additional pointers, 
`left` and `right`, to search for the other two numbers.

3. The Two-Pointer Sub-problem:
   - The `left` pointer starts at `idx + 1` and the `right` pointer starts at the end of the array.
   - We calculate the sum of the three numbers: `nums[idx] + nums[left] + nums[right]`.
   - If the sum is less than zero, we need a larger value, so we increment `left`.
   - If the sum is greater than zero, we need a smaller value, so we decrement `right`.
   - If the sum is exactly zero, we've found a valid triplet. We add it to our result list and then move both 
   `left` and `right` pointers inward.

4. Handling Duplicates: To ensure our result contains only unique triplets, we add checks to skip over duplicate numbers.
We do this for the main `idx` pointer and also for the `left` and `right` pointers after finding a valid triplet.

Why it works:
This approach is a clever extension of the Two-Sum problem. By fixing one element and using the two-pointer technique 
on the rest of the sorted array, we reduce the time complexity from O(n³) (brute-force) to O(n²) because the inner 
two-pointer loop runs in O(n) time. The initial sort adds an O(n log n) cost, but the overall complexity remains 
efficient.
"""