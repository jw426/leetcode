class Solution(object):

    conv = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        combs = ['']
        for num in digits:
            temp = []
            for prev in combs: 
                for ch in self.conv[num]:
                    temp.append(prev + ch)
            
            combs = temp
        
        return combs
            




        