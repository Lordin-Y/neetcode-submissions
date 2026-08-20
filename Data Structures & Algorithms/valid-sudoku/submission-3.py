class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #append is for list, add is for sets
        #have a board where we don't want duplicates in rows, cols, and boxes
        #create a list with a set inside
        row_set = []
        col_set = []
        box_set = []
        #create a set for each set to catch duplicates
        for i in range(len(board)):
            row_set.append(set())
            col_set.append(set())
            box_set.append(set())
        for row in range(len(board)):
            for col in range(len(board)):
                number = board[row][col]
                if number == ".":
                    continue
                box_index = (row//3) *3 + (col//3)
                if number in row_set[row] or number in col_set[col] or number in box_set[box_index]:
                    return False
                else:
                    row_set[row].add(number)
                    col_set[col].add(number)
                    box_set[box_index].add(number)
        return True