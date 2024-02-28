class Solution:

    roman_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    
    def intToRoman(self, num: int) -> str:
    
        roman = ""
    
        for val, sym in self.roman_dict.items():
            temp = ""
            exp = 0
            # appending roman characters naively
            while num - val >= 0:
                temp += sym
                num -= val
            
            # collapsing roman chars 
            if len(temp) == 4:
                temp = sym + self.roman_dict[5*val]
            
            roman += temp
        return roman


        
obj = Solution()
print(obj.intToRoman(1994))