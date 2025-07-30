"""
Problem Statement -> Given an array of integers that are out of order, we need to find smallest window that must 
be sorted in order for the entire array to be sorted.

i/p -> [3,7,5,6,9]
o/p -> (1,3)
"""
def window(lst):
    left, right = None, None
    s = sorted(lst)

    for i in range(len(lst)):
        if lst[i] != s[i] and left is None:
            left = i
        elif lst[i] != s[i]:
            right = i
    return left, right

ip_lst = [3,7,5,6,9]
print(window(ip_lst))
