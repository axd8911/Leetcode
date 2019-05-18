'''
70%

A very compresensive backtracking question. Looked at YouTube videos. Worth retry.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        found = False
        
        def bt(x,y,d):
            if x>=len(board[0]) or y>=len(board) or x<0 or y<0 or word[d]!=board[y][x]:
                return False
            if word[d] == board[y][x]:
                temp = board[y][x]
                board[y][x] = None
            if d == len(word) - 1:
                return True
            found = bt(x+1,y,d+1) or bt(x,y+1,d+1) or bt(x-1,y,d+1) or bt(x,y-1,d+1)
            board[y][x]=temp
            return found
        
        for i in range(len(board[0])):
            for j in range(len(board)):
                found = bt(i,j,0)
                if found == True:
                    return found
                
        return found
            
        
