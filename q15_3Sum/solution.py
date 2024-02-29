class Solution(object):

    conv = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # base case
        if digits <= 1: 
            return [""]
        
        prev = self.letterCombinations(int(digits/10))
        curr = []
        for ch in self.conv[digits % 10]:
            for p_ch in prev:
                curr.append(p_ch + ch)
        
        return curr

obj = Solution()
print(obj.letterCombinations(0))
    




        