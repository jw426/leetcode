class Solution:
    DIGIT = 9
    GRID = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = ["" for _ in range(self.DIGIT)]
        col = ["" for _ in range(self.DIGIT)]
        box = ["" for _ in range(self.DIGIT)]

        for i_row in range(self.DIGIT):
            for i_col in range(self.DIGIT): 
                cell = board[i_row][i_col]
                if (self.repeated(row, i_row, cell) or 
                    self.repeated(col, i_col, cell) or
                    self.repeated(box, (i_row // self.GRID) * self.GRID + i_col // self.GRID, cell)):
                    print(row, i_row)
                    print(col, i_col)
                    print(box)
                    print(cell)
                    return False
    
    def repeated(self, block, i, add_new):

        if add_new == '.':
            return False

        if add_new in block[i]:
            print(add_new, block[i])
            return True

        block[i] += add_new
        



             
        