class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1:
            return s

        pattern = ["" for _ in range(numRows)]
        idx = 0
        add = -1
        for ch in s:
            pattern[idx] += ch
            add = -add if idx in [0, numRows - 1] else add
            idx += add 
        
        return ''.join(pattern)


obj = Solution()
print(obj.convert("A", 1))
        