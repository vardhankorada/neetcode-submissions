class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            temp = set()
            for j in range(len(board[0])): 
                if row[j] in temp and row[j]!=".": 
                    return False
                else: temp.add(row[j])
        for j in range(len(board[0])):
            temp = set()
            for i in range(len(board)):
                if board[i][j] in temp and board[i][j] != ".":
                    return False
                else: temp.add(board[i][j])
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                corner = (i,j)
                temp = set()
                for k in range(0,3):
                    for l in range(0,3):
                        if board[i+k][j+l] in temp and board[i+k][j+l]!=".": 
                            return False
                        else: temp.add(board[i+k][j+l])
        return True