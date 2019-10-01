class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i,j,idx):
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or word[idx]!=board[i][j]:
                return False
            if word[idx]==board[i][j]:
                temp=board[i][j]
                board[i][j] = None
            if idx==len(word)-1:
                return True
            found = helper(i+1,j,idx+1) or helper(i,j+1,idx+1) or helper(i-1,j,idx+1) or helper(i,j-1,idx+1)
            board[i][j]=temp
            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,0):
                    return True
        return False
