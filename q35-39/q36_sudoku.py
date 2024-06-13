from collections import defaultdict
class Solution:
    DIGIT = 9
    GRID = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # hardcoding is most efficient
        # since sudoku is 9x9

        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        for i_row in range(self.DIGIT):
            for i_col in range(self.DIGIT): 
                cell = board[i_row][i_col]
                
                if cell == '.':
                    continue 

                if (self.repeated(row, i_row, cell) or 
                    self.repeated(col, i_col, cell) or
                    self.repeated(sqr, (i_row // self.GRID, i_col // self.GRID), cell)):
                    return False
                
        return True
    
    def repeated(self, block, i, add_new):

        if add_new in block[i]:
            return True

        block[i].add(add_new)
        



             
        