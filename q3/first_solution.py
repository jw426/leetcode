from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_dict = defaultdict(lambda: -1)
        
        max_length = 0
        cur_start = 0

        # "abcabcabc"
        for i in range(0, len(s)):

            # repeating character
            if char_dict[s[i]] >= cur_start:
                cur_start = char_dict[s[i]] + 1
                char_dict[s[i]] = i
            
            # non-repeating
            else: 
                char_dict[s[i]] = i

            # current string observed is the maximum length
            if i - cur_start + 1 > max_length:
                max_length = i - cur_start + 1
                
        return max_length

