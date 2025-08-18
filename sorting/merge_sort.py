def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    return merge(merge_sort(arr[:mid]),merge_sort(arr[mid:]))

def merge(left_half,right_half):
    left_idx = 0
    right_idx = 0
    result = []

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] <= right_half[right_idx]:
            result.append(left_half[left_idx])
            left_idx += 1
        else:
            result.append(right_half[right_idx])
            right_idx += 1

    while left_idx < len(left_half):
        result.append(left_half[left_idx])
        left_idx += 1
    
    while right_idx < len(right_half):
        result.append(right_half[right_idx])
        right_idx += 1
    
    return result


arr = [8,5,2,9,5,6,3]
print(merge_sort(arr))
