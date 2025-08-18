def quick_sort(array):
    quick_sort_helper(array,0,len(array)-1)
    return array

def quick_sort_helper(array, start_idx, end_idx):

    if start_idx >= end_idx:
        return
    
    right_idx = end_idx
    pivot_idx = start_idx
    left_idx = start_idx + 1

    while left_idx <= right_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(array,left_idx,right_idx)
        elif array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        elif array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    
    swap(array,pivot_idx,right_idx)

    left_subarray_is_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)
    if left_subarray_is_smaller:
        quick_sort_helper(array, start_idx, right_idx - 1)
        quick_sort_helper(array, right_idx + 1, end_idx)
    else:
        quick_sort_helper(array, right_idx + 1, end_idx)
        quick_sort_helper(array, start_idx, right_idx - 1)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

arr = [8,5,2,9,5,6,3]
print(quick_sort(arr))