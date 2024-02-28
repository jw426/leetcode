class Solution:

    roman_conv = {'I': 'X', 'X': 'C', 'C': 'M', 'V': 'L', 'L': 'D'}

    # takes in roman characters
    # returns roman characters if original was multiplied by 10
    def multRoman(self, roman: str) -> str:

        new_roman = ""
        for ch in roman: 
            new_roman += self.roman_conv[ch]
        
        return new_roman
    
    # converts one-digit integer to roman character
    def singleIntToRoman(self, num: int) -> str:
        roman_valsym = [(5, 'V'), (1, 'I')]

        if num == 4: 
            return "IV"
        elif num == 9:
            return "IX"
        
        roman = ""
        for val, sym in roman_valsym:
            while num - val >= 0:
                roman += sym
                num -= val 
        
        return roman

    def intToRoman(self, num: int) -> str:
    
        roman = ""
        for n in str(num):
            roman = self.multRoman(roman)
            roman += self.singleIntToRoman(int(n))
            
        return roman


        
obj = Solution()
print(obj.intToRoman(1994))