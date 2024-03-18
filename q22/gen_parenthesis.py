class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def genRec(count = 0, s = ''):

            if len(s) > n*2:
                return 

            if len(s) == n*2 and count == 0:
                curr.append(s)
                return
            
            genRec(count + 1, s + '(')
            if count > 0:
                genRec(count - 1, s + ')')  
    
        curr = []
        genRec()
        return curr
        
    