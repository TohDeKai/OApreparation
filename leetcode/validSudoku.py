# https://leetcode.com/problems/valid-sudoku/description/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Have 3 hashmaps to keep track of the numbers that has appeared
        hm row - key will be row, value will be a set. set is the number that has appeared in that row
        hm col - same but col
        hm squares - will be same but as square. key will be split into [0,0] to [2,2].
        """
        row = {}
        col = {}
        squares = {}

        r = c = 0
        while r < len(board):
            while c < len(board[0]):
                if board[r][c] != ".":
                    if r in row:
                        if board[r][c] in row[r]:
                            return False
                    else:
                        row[r] = []
                    row[r].append(board[r][c])

                    if c in col:
                        if board[r][c] in col[c]:
                            return False
                    else:
                        col[c] = []
                    col[c].append(board[r][c])

                    if (r // 3, c // 3) in squares:
                        if board[r][c] in squares[(r // 3, c // 3)]:
                            return False
                    else:
                        squares[(r // 3, c // 3)] = []
                    squares[(r // 3, c // 3)].append(board[r][c])
                c += 1
            r += 1
            c = 0

        return True
