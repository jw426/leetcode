class Solution:

    def check(self, sch, pch) -> bool:
        if pch == '.': return True
        if sch == pch: return True
        return False

    def reduce(self, p) -> str:

        j = 0
        while j+3 < len(p):
            if p[j:j+2] == p[j+2:j+4] and p[j+1] == '*':
                p = p[:j+2] + p[j+4:]
                continue 
            j += 1

        return p

    def isMatch(self, s: str, p: str) -> bool:
        
        j = 0
    
        p = self.reduce(p)
        for i in range(len(p)): 

            pch = p[i]

            # pattern is *
            if pch == '*':
                
                prev = p[i-1]
                if i == 0 or prev == '*': 
                    continue 
                
                # repeating 'prev' character
                # many versions exist 
                # parse through all versions 
                # with list 
                iterlist = [self.isMatch(s[j:], p[i+1:])]
                while j < len(s) and self.check(s[j], prev):
                    iterlist.append(self.isMatch(s[j+1:], p[i+1:]))
                    j += 1

                return any(iterlist)

            # pattern is . or alphabet
            else:
                if i < len(p) - 1 and p[i+1] == '*': 
                    continue
                
                if j == len(s) or (j < len(s) and not self.check(s[j], pch)):
                    return False 

                j += 1   

        return len(s[j:]) == 0
                