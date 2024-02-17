import sys

class Solution:
    def reverse(self, x: int) -> int:
        
        int_str = str(x)
        reversed = 0
        digit = 0
    
        for i in range(len(int_str)-1,-1,-1):

            if int_str[i] == '-':
                reversed *= -1
                break
            
            digit = int(int_str[i])
            if reversed > (2**31 - 1) / 10 or (reversed == (2**31 - 1) / 10 and digit > 7):
                return 0
            if reversed < (-2**31) / 10 or (reversed == (-2**31) / 10 and digit > 8):
                return 0
            
            reversed = reversed * 10 + digit
                  
            

        return reversed 
    
obj = Solution()
print(obj.reverse(-123))