"""
Problem Statement -> Given an array of integers , return a new array such that each element at index i of 
the given array is the product of all the numbers in the original array except the one at i.

i/p -> [1,2,3,4,5]
o/p -> [120, 60, 40, 30, 24]

i/p  -> [3,2,1]
o/p -> [2,3,6]
"""

def get_products(nums):
    # generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    
    # generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    
    suffix_products = list(reversed(suffix_products))

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[1])
        elif i == len(nums) - 1:
            result.append(prefix_products[-2])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    return result

input_1 = [1,2,3,4,5]
print(get_products(input_1))

input_2 = [3,2,1]
print(get_products(input_2))