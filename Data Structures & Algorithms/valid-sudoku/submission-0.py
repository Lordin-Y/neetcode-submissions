class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #append is list only
        #add is set only
        row_set = []
        col_set = []
        box_set = []
        for i in range(len(board)):
            row_set.append(set())
            col_set.append(set())
            box_set.append(set())
        for row in range(len(board)):
            for col in range(len(board)):
                box_index = (row //3) *3 + (col //3)
                digit = board[row][col]
                if digit == ".":
                    continue
                if digit in row_set[row] or digit in col_set[col] or digit in box_set[box_index]:
                    return False
                else:
                    row_set[row].add(digit)
                    col_set[col].add(digit)
                    box_set[box_index].add(digit)
        return True
        
        