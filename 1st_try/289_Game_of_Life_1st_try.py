class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live cell has <2 or >3 neighbors: it dies
        # live cell has 2 or 3 neighbors: it still lives
        # die cell has 3 neighbors live: it lives
        # live but now die: 1 to -1
        # live and still live: 1 to 1
        # die and still die: 0 to 0
        # die but now live: 0 to 2
        # count all cells: -1 and 1 contribute live, 0 and 2 contribute die
        # convert -1 to die and convert 2 to live

        directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                for dx,dy in directions:
                    if 0<=i+dx<len(board) and 0<=j+dy<len(board[0]) and (board[i+dx][j+dy]==1 or board[i+dx][j+dy]==-1):
                        live += 1

                if board[i][j] == 1 and (live>3 or live<2):
                    board[i][j] = -1
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


                
