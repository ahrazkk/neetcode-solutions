class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print(board)
        hashMap = set()

        for row in board:
            print(row)
            for number in row:
                print(number)
                if number == ".":
                    continue # Skip empty cells
                
                if number in hashMap:
                    return False
                    continue
                if board[0][number]
        if row[-1] != False:
            return True