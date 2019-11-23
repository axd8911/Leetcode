class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        h,w = len(board),len(board[0])

        for i in range(h):
            for j in range(w):
                live = 0
                for dx,dy in directions:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<h and 0<=ny<w and (board[nx][ny] == 1 or board[nx][ny] == -1):
                        live += 1
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and not 2<=live<=3:
                    board[i][j] = -1

        for i in range(h):
            for j in range(w):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
        return board
