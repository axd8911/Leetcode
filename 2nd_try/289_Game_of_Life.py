class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        h,w = len(board),len(board[0])
        for i in range(h):
            for j in range(w):
                live = 0
                for dx,dy in direction:
                    if 0<=i+dx<h and 0<=j+dy<w and (board[i+dx][j+dy]==1 or board[i+dx][j+dy]==-1):
                        live+=1
                if board[i][j] == 1 and (live<2 or live>3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live==3:
                    board[i][j] = 2

        for i in range(h):
            for j in range(w):
                if board[i][j]==-1:
                    board[i][j] = 0
                elif board[i][j]==2:
                    board[i][j]=1
                    
