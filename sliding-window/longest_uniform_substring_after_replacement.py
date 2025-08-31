"""
Problem Statement -> Given a string , determine the length of the longest uniform substring that can be formed by replacing
                     up to k characters.

What is uniform substring ?
A uniform substring is one in which all the characters are identical.
"""

def longest_uniform_substring_after_replacement(s:str, k:int) -> int:
    freqs = {}
    left = right = 0
    highest_freq = max_len = 0

    while right < len(s):
        freqs[s[right]] = freqs.get(s[right],0) + 1
        highest_freq = max(highest_freq, freqs[s[right]])
        num_chars_to_replace = (right - left + 1) - highest_freq

        if num_chars_to_replace > k:
            freqs[s[left]] -= 1
            left += 1
        max_len = right - left + 1
        right += 1
    return max_len

print(longest_uniform_substring_after_replacement("aabcdcca",2))