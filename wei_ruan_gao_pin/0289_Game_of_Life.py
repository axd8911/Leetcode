class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 is dead 1 is live -1 is live to dead -2 is dead to live
        
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                for dx,dy in directions:
                    if 0<=i+dx<len(board) and 0<=j+dy<len(board[0]):
                        if board[i+dx][j+dy]==1 or board[i+dx][j+dy]==-1:
                            count += 1
                if board[i][j]==1 and (count<2 or count>3):
                    board[i][j] = -1
                elif board[i][j]==0 and count==3:
                    board[i][j] = -2
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -2:
                    board[i][j]=1
                elif board[i][j] == -1:
                    board[i][j] = 0
        
