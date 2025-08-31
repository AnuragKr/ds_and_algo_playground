"""
Problem Statement -> Given two strings, s and t, both consisting of lowercase English letters, return the number of 
substrings in s that are anagrams of t.
"""

def substring_anagrams(s:str,t:str) -> int:
    len_s, len_t = len(s), len(t)
    left,right = 0,0
    count = 0

    expected_freq, window_freq = [0]*26, [0]*26

    for c in t:
        expected_freq[ord(c) - ord('a')] += 1

    while right < len_s:
        window_freq[ord(s[right]) - ord('a')] += 1

        if right - left + 1 == len_t:
            if window_freq == expected_freq:
                count += 1
            window_freq[ord(s[left]) - ord('a')] -= 1
            left += 1
        right += 1
    return count

s = 'caabab'
t = 'aba'
print(substring_anagrams(s,t))
