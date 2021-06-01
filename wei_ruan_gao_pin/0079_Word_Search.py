class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        self.output = False
        
        def backtracking(x,y,visited,comb,idx):
            if comb == word:
                self.output = True
                return
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                return
            if (x,y) in visited:
                return
            if board[x][y]!=word[idx]:
                return
            comb += board[x][y]
            visited.add((x,y))
            for dx,dy in directions:
                backtracking(x+dx,y+dy,visited,comb,idx+1)
            visited.remove((x,y))
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] ==word[0]:
                    print (i,j)
                    backtracking(i,j,set(),'',0)
        
        return self.output
