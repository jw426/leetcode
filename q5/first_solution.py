from collections import defaultdict

class Solution(object):

    def expand(self, s, i):

        if i % 1 == 0:
            l = r = i
        else:
            l = i - 0.5
            r = i + 0.5

        while (l >= 0 and r < len(s)):
            # print(s, int(l), int(r))
            if s[int(l)] == s[int(r)]:
                l-=1
                r+=1
            else:
                break 
    
        return r - l - 1
        

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 : return s

        max_len = 1;
        mid_idx = 0;

        for i in range(1,len(s)*2):

            new_exp = self.expand(s,float(i)/2)
            print(new_exp)
            if max_len < new_exp:
                max_len = new_exp
                mid_idx = float(i)/2
        
        # print(max_len, mid_idx)

        lower_idx = int(math.ceil(mid_idx-max_len/2))
        # print(type(lower_idx))
        return s[int(lower_idx) : int(lower_idx + max_len)]




        



        

