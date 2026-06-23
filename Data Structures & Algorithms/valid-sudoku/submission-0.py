class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(9):
            rows=[]
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in rows:
                    return False
                else:
                    rows.append(board[i][j])
        #check cols
        for i in range(9):
            cols=[]
            for j in range(9):
                if board[j][i]==".":
                    continue
                elif board[j][i] in cols:
                    return False
                else:
                    cols.append(board[j][i])    
        #check boxes
        box_start=[(0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6)]
        for i,j in box_start:
            boxes=[]
            for a in range(i,i+3):
                for b in range(j,j+3):
                    if board[a][b]==".":
                        continue
                    elif board[a][b] in boxes:
                        return False
                    else:
                        boxes.append(board[a][b])
        return True


