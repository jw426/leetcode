class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
         
        # base case
        if n == 1: 
            return ["()"]
        
        # solve with recursion
        prev = self.generateParenthesis(n-1)
        curr = []
        if not (n % 2):
            line = ""
            line2 = ""
            for _ in range(n/2):
                line += '('
                line2 += ')'
            curr.append((line + line2) * 2)

            
        for i in prev:
            # append outer
            curr.append('(' + i + ')')
            # append beside (left & right)
            left = '()' + i
            rght = i + '()'
            curr.append(rght)
            if left != rght:
                curr.append(left)
    
        return set(curr)