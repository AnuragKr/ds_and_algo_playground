"""
Problem Statement -> Given a string determine the length of its longest substring that consists only of unique characters
"""
def longest_substring_with_unique_chars(s:str):
    left = right = 0
    max_count = 0
    hash_set = set()

    while right < len(s):

        while s[right] in hash_set:
            hash_set.remove(s[left])
            left += 1

        max_count = max(max_count, len(hash_set))
        print(hash_set)
        hash_set.add(s[right])
        right += 1
    
    return max_count

def longest_substring_with_unique_chars_optimized(s:str):
    left = right = 0
    max_count = 0
    prev_indexes = {}

    while right < len(s):
        
        if s[right] in prev_indexes and prev_indexes[s[right]] >= left:
            left = prev_indexes[s[right]] + 1

        max_count = max(max_count, right - left + 1)
        prev_indexes[s[right]] = right
        right += 1
    
    return max_count

print(longest_substring_with_unique_chars_optimized("cabcdeca"))

