"""
Problem Statement -> Given an array of integers, return all triplets [a,b.c] such that a+b+c=0.The solution must not
contain duplicate triplets. If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

i/p -> array = [0,-1,2,-3,1]
o/p -> [[-3,1,2], [-1,0,1]]
"""

"""
Pattern -> Two Pointer Problem

The core idea is to leverage idea of Two Pair Sum solution to solve this triplet sum. 
If our input is [a,b,c] then we need to find Two Pair Sum [b,c] which should sum up to -a.
Next we need to make sure triplets should not be repeated for this make sure -
  1.) a -> First element should not be repeated, if we find a again in array then we should skip it
      Ex- [-4,-4,-2,0,0,1,3]. -4-> a is repeated twice second time it won't be considered.
  2.) b -> Second element should not be repeated, if we find b again in array then we should skip it and this 
           condition should be taken care in Two Pair Sum function.
      Ex- [-4,-4,-2,0,0,1,3]. -2-> a, 0-> b is repeated twice second time 0 for b won't be considered.
  3.) Once a and b are unique then triplet [a,b,c] will be unique.
Also if input is positive then we can skip calling Two Pair Sum as positive elements won't sum up to 0. Since 
we have sorted the array then we can consider that further elements will all be positive.
Ex -> [1,2,3,4,5] 
"""

def triplet_sum(nums):
    result = []
    nums.sort()
    for idx in range(0,len(nums)-2):
       if nums[idx] > 0:
           break
       
       if idx > 0 and nums[idx] == nums[idx-1]:
            continue
       
       pairs = pair_sum_sorted(nums[idx+1:],-nums[idx])
       for pair in pairs:
           result.append([nums[idx]] + pair)
    
    return result

def pair_sum_sorted(nums,target):
    left = 0
    right = len(nums) - 1
    result = []

    while left < right:
        pair_sum = nums[left] + nums[right]
        if  pair_sum < target:
            left += 1
        elif pair_sum > target:
            right -= 1
        else:
            result.append([nums[left],nums[right]])
            left += 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
    
    return result

# print(triplet_sum([0,-1,2,-3,1]))